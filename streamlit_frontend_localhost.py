# import pysqlite3
# import sys
# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
# import sqlite3
import streamlit as st
from vector_store import FlowerShopVectorStore
from chatbot import app
from langchain_core.messages import AIMessage, HumanMessage
from tools import customers_database, data_protection_checks

#from streamlit_navigation_bar import st_navbar

st.set_page_config(layout='wide', page_title='Flower Shop Chatbot', page_icon='💐',initial_sidebar_state="collapsed" )

#Navbar
from streamlit_option_menu import option_menu
selected = option_menu(
   menu_title=None,  # No title to make it look like a navbar
   options=["Home", "Documentation", "Examples", "Community", "About"],
   icons=["house", "book", "code", "people", "info"],  # Optional Bootstrap icons
   menu_icon="cast",
   default_index=0,
   orientation="horizontal",
)

# Hide sidebar
st.markdown(
    """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
    </style>
    """,
    unsafe_allow_html=True,
)
# 3. Show which page is selected (for testing)
st.write(f"You selected {selected}")

# Home page content
if selected == "Home":
    st.switch_page(f"pages/home.py")

# Handle navigation
else:
   st.switch_page(f"pages/{selected.lower()}.py")


    #st.title("Welcome to the Flower Shop Chatbot")
# Your existing chat interface code here


# if 'message_history' not in st.session_state:
#     st.session_state.message_history = [AIMessage(content="Hiya, Im the flower shop chatbot. How can I help?")]

# left_col, main_col, right_col = st.columns([1, 2, 1])

# # 1. Buttons for chat - Clear Button

# with left_col:
#     if st.button('Clear Chat'):
#         st.session_state.message_history = []


# # 2. Chat history and input
# with main_col:
#     user_input = st.chat_input("Type here...")

#     if user_input:
#         st.session_state.message_history.append(HumanMessage(content=user_input))

#         response = app.invoke({
#             'messages': st.session_state.message_history
#         })

#         st.session_state.message_history = response['messages']

#     for i in range(1, len(st.session_state.message_history) + 1):
#         this_message = st.session_state.message_history[-i]
#         if isinstance(this_message, AIMessage):
#             message_box = st.chat_message('assistant')
#         else:
#             message_box = st.chat_message('user')
#         message_box.markdown(this_message.content)
# # 3. State variables

# with right_col:
#     st.title('customers database')
#     st.write(customers_database)
#     st.title('data protection checks')
#     st.write(data_protection_checks)

