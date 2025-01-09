
import os

# with open(".env", "r") as f:
#     for line in f:
#         key, value = line.split("=")
#         os.environ[key] = value.strip()

import streamlit as st
from caller_agent import CONVERSATION, receive_message_from_caller
from appointment_tools import APPOINTMENTS
from langchain_core.messages import HumanMessage
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

col1, col2 = st.columns(2)

with col1:
    st.subheader("Appointment Manager")

    for message in CONVERSATION:
        if type(message) == HumanMessage:
            with st.chat_message("user"):
                st.write(message.content)
        else:
            with st.chat_message("assistant"):
                st.write(message.content)
    
    message = st.chat_input("Type message here", on_submit=submit_message, key="message")


with col2:
    st.header("Appointments")
    st.write(APPOINTMENTS)