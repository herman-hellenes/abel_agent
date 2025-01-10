
import os

# with open(".env", "r") as f:
#     for line in f:
#         key, value = line.split("=")
#         os.environ[key] = value.strip()

import streamlit as st
from caller_agent import CONVERSATION, receive_message_from_caller, caller_app
from appointment_tools import APPOINTMENTS
from langchain_core.messages import HumanMessage,  AIMessage

import langsmith

langsmith.debug = True                                                   

from streamlit_option_menu import option_menu
st.set_page_config(layout='wide', page_title='Cartwheel | Appointment Demo', page_icon='🤸',initial_sidebar_state="collapsed" )

#Navbar
from streamlit_option_menu import option_menu
selected = option_menu(
   menu_title=None,  # No title to make it look like a navbar
   options=["Home", "Logic Setup", "Resources Setup", "Evaluate","Demo","Appointment"],
   icons=["house", "book", "code", "people", "info"],  # Optional Bootstrap icons
   menu_icon="cast",
   default_index=5,
   orientation="horizontal",
)

if "selected" not in st.session_state:
   st.session_state.selected = "Appointment"
if selected != st.session_state.selected:
   st.session_state.selected = selected
   #st.switch_page(f"pages/{selected.lower()}.py")
   st.switch_page(f"pages/{selected.lower().replace(' ', '')}.py")

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

# Documentation content
#st.title("Documentation", anchor=False)
st.markdown("<h1 style='text-align: center;'>Dr Appointment Manager</h1>", unsafe_allow_html=True)

st.markdown("Here you can book your doctor's appointment by talking to our agent. You can also check next available time, cancel your appointsment, etc. ", unsafe_allow_html=True)


def submit_message():
    receive_message_from_caller(st.session_state["message"])

#left_col, col1, col2 = st.columns(3)
left_col, main_col, right_col = st.columns([1, 2, 1])
if 'message_history' not in st.session_state:
    st.session_state.message_history = [AIMessage(content="Hi, please let me help you booking an appointment for you. What could be a suitable time? ")]


with left_col:
    if st.button('Clear Chat'):
        st.session_state.message_history = []

with main_col:
    st.subheader("Appointment Manager")

    for message in CONVERSATION:
        if type(message) == HumanMessage:
            with st.chat_message("user"):
                st.write(message.content)
        else:
            with st.chat_message("assistant"):
                st.write(message.content)
    
    message = st.chat_input("Type message here", on_submit=submit_message, key="message")

# with main_col:
#     st.subheader("Appointment Manager")
#     user_input = st.chat_input("Type here...")

#     if user_input:
#         st.session_state.message_history.append(HumanMessage(content=user_input))

#         response = caller_app.invoke({
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


with right_col:
    st.header("Appointments")
    st.write(APPOINTMENTS)


    