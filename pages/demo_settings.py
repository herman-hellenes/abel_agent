import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import json

# Keep the same navbar for consistency
st.set_page_config(layout='wide', page_title='Cartwheel | Demo Settings', page_icon='🤸',initial_sidebar_state="collapsed")

# Move this initialization before the option_menu
#if "selected" not in st.session_state:
#   st.session_state.selected = "Documentation"

selected = option_menu(
   menu_title=None,  # No title to make it look like a navbar
   options=["Home", "Demo", "Resources", "Contact", "Demo_settings"],
   icons=["house", "book", "code", "people", "info"],  # Optional Bootstrap icons
   menu_icon="cast",
   default_index=4,
   orientation="horizontal",
)


# This initialization happens AFTER the menu selection
if "selected" not in st.session_state:
   st.session_state.selected = "Demo_settings"
if selected != st.session_state.selected:
   st.session_state.selected = selected
   st.switch_page(f"pages/{selected.lower()}.py")
   # if selected == "Home":
   #     st.switch_page("pages/home.py")
   # else:
   #     st.switch_page(f"pages/{selected.lower()}.py")


# Start Prompt to bot
#################
st.markdown("<h3 style='text-align: center;'> Start Prompt to agent </h3>", unsafe_allow_html=True)

with open("prompt_xc.txt", 'r') as file:
      content = file.read()

# Display the text content
st.text_area("Prompt Content", content, height=300) 
# Inventory
#################
st.markdown("<h3 style='text-align: center;'> Inventory </h3>", unsafe_allow_html=True)

# Load the JSON data from the file
with open('inventory_xc.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data) 
# df = pd.DataFrame(
#     [
#         {"command": "st.selectbox", "rating": 4, "is_widget": True},
#         {"command": "st.balloons", "rating": 5, "is_widget": False},
#         {"command": "st.time_input", "rating": 3, "is_widget": True},
#     ]
# )
#st.dataframe(df, use_container_width=True)
st.data_editor(df, use_container_width=True)

# Q&A to bot
#################
st.markdown("<h3 style='text-align: center;'> FAQ agent setup </h3>", unsafe_allow_html=True)

# Load the JSON data from the file
with open('FAQ_xc.json', 'r') as f:
    data_faq = json.load(f)
df_faq = pd.DataFrame(data_faq) 
# df = pd.DataFrame(
#     [
#         {"command": "st.selectbox", "rating": 4, "is_widget": True},
#         {"command": "st.balloons", "rating": 5, "is_widget": False},
#         {"command": "st.time_input", "rating": 3, "is_widget": True},
#     ]
# )
#st.dataframe(df, use_container_width=True)
st.data_editor(data_faq, use_container_width=True)
