import pysqlite3
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import sqlite3
import streamlit as st
from vector_store import ShopVectorStore
from chatbot import app
from langchain_core.messages import AIMessage, HumanMessage
from tools import customers_database, data_protection_checks

#from streamlit_navigation_bar import st_navbar

st.set_page_config(layout='wide', page_title='Cartwheel', page_icon='🤸',initial_sidebar_state="collapsed" )

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

