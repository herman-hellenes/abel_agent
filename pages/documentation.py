import streamlit as st
from streamlit_option_menu import option_menu
# Keep the same navbar for consistency
st.set_page_config(layout='wide', page_title='Documentation - Flower Shop Chatbot', page_icon='💐',initial_sidebar_state="collapsed")

if "selected" not in st.session_state:
   st.session_state.selected = "Documentation"
selected = option_menu(
   menu_title=None,
   options=["Home", "Documentation", "Examples", "Community", "About"],
   icons=["house", "book", "code", "people", "info"],
   menu_icon="cast",
   default_index=1,  # Documentation is selected by default
   orientation="horizontal",
   key="nav" 
)


if selected != st.session_state.selected:
   st.session_state.selected = selected
   st.switch_page(f"pages/{selected.lower()}.py")
   # if selected == "Home":
   #     st.switch_page("pages/home.py")
   # else:
   #     st.switch_page(f"pages/{selected.lower()}.py")

# Documentation content
st.title("Documentation")
st.write("Here's the documentation for our Flower Shop Chatbot...")