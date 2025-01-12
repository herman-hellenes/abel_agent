import streamlit as st
from vector_store import FlowerShopVectorStore
from chatbot import app
from langchain_core.messages import AIMessage, HumanMessage
from tools import customers_database, data_protection_checks, orders_database
from streamlit_extras.add_vertical_space import add_vertical_space
import mypaths
st.set_page_config(layout='wide', page_title='Cartwheel | Everlyn Demo', page_icon='🤸',initial_sidebar_state="collapsed" )

# #SETTING AGENT TYPE: TODO!!
# AGENT_TYPES = ["flower_shop", "xc_sport"]
# # Store in session state to persist across reruns
# if 'AGENT_TYPE' not in st.session_state:
#     st.session_state.AGENT_TYPE = AGENT_TYPES[0]

# # Create dropdown and update session state when changed
# selected_type = st.selectbox(
#     "Select Agent Type",
#     options=AGENT_TYPES,
#     index=AGENT_TYPES.index(st.session_state.AGENT_TYPE)
# )

# # Update session state if selection changes
# if selected_type != st.session_state.AGENT_TYPE:
#     st.session_state.AGENT_TYPE = selected_type
#     st.rerun()  # Force a rerun to update everything


# # Display current agent type
# st.write(f"Current Agent Type: {st.session_state.AGENT_TYPE}")

#from streamlit_navigation_bar import st_navbar


# #Navbar
# from streamlit_option_menu import option_menu
# selected = option_menu(
#    menu_title=None,  # No title to make it look like a navbar
#    options=["Home", "Logic Setup", "Resources Setup", "Evaluate","Demo","Appointment"],
#    icons=["house", "book", "code", "people", "info"],  # Optional Bootstrap icons
#    menu_icon="cast",
#    default_index=4,
#    orientation="horizontal",
# )

# if "selected" not in st.session_state:
#    st.session_state.selected = "Demo"
# if selected != st.session_state.selected:
#    st.session_state.selected = selected
#    #st.switch_page(f"pages/{selected.lower()}.py")
#    st.switch_page(f"pages/{selected.lower().replace(' ', '')}.py")

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
#st.write(f"You selected {selected}")
# Handle navigation


with open(mypaths.GREETING, 'r') as file:
      greeting_msg = file.read()
if 'message_history' not in st.session_state:
    st.session_state.message_history = [AIMessage(content=greeting_msg)]

left_col, main_col, right_col = st.columns([1, 2, 1])

# 1. Buttons for chat - Clear Button

with left_col:
    if st.button('Clear Chat'):
        st.session_state.message_history = []


# 2. Chat history and input
def get_text_value(data):
  """
  Extracts the 'text' value from the input data.

  Args:
    data: The input data, which can be either a string or a list of dictionaries.

  Returns:
    The 'text' value if found, otherwise the original data.
  """

  if isinstance(data, str):
    return data

  for item in data:
    if isinstance(item, dict) and 'text' in item:
      return item['text']

  return data


with main_col:
    user_input = st.chat_input("Type here...")

    if user_input:
        st.session_state.message_history.append(HumanMessage(content=user_input))

        response = app.invoke({
            'messages': st.session_state.message_history
        })

        st.session_state.message_history = response['messages']

    for i in range(1, len(st.session_state.message_history) + 1):
        this_message = st.session_state.message_history[-i]
        if isinstance(this_message, AIMessage):
            message_box = st.chat_message('assistant', avatar="🤸")
            message_box.markdown(get_text_value(this_message.content))
        elif isinstance(this_message, HumanMessage):
            message_box = st.chat_message('user', avatar="✌")
            message_box.markdown(get_text_value(this_message.content))
        #else:
        #    message_box = st.chat_message('user', avatar="🚶")
        #    message_box.markdown(get_text_value(this_message.content))
        #message_box.markdown(get_text_value(this_message.content))



from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.row import row
footer_html = """<div style='text-align: center;'>
  <p>Powered by AbelAI </p>
</div>"""
st.markdown(footer_html, unsafe_allow_html=True)


