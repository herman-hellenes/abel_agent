from langgraph.graph import StateGraph, MessagesState
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic  
from langgraph.prebuilt import ToolNode
from tools import query_knowledge_base, search_for_product_reccommendations, data_protection_check, create_new_customer, place_order, retrieve_existing_customer_orders

import os
from dotenv import load_dotenv
load_dotenv() 

import mypaths
with open(mypaths.PERSONA, 'r') as file:
      prompt = file.read()

chat_template = ChatPromptTemplate.from_messages(
    [
        ('system', prompt),
        ('placeholder', "{messages}")
    ]
)

tools = [query_knowledge_base, search_for_product_reccommendations, data_protection_check, create_new_customer, place_order, retrieve_existing_customer_orders]

llm = ChatAnthropic(
   model="claude-3-haiku-20240307"   
)
llm_with_prompt = chat_template | llm.bind_tools(tools)


def call_agent(message_state: MessagesState):
    
    response = llm_with_prompt.invoke(message_state)

    return {
        'messages': [response]
    }

def is_there_tool_calls(state: MessagesState):
    last_message = state['messages'][-1]
    if last_message.tool_calls:
        return 'tool_node'
    else:
        return '__end__'


graph = StateGraph(MessagesState)

tool_node = ToolNode(tools)

graph.add_node('agent', call_agent)
graph.add_node('tool_node', tool_node)

graph.add_conditional_edges(
    "agent",
    is_there_tool_calls
)
graph.add_edge('tool_node', 'agent')

graph.set_entry_point('agent')

app = graph.compile()

