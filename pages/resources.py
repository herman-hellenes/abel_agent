import streamlit as st
from streamlit_option_menu import option_menu
# Keep the same navbar for consistency
st.set_page_config(layout='wide', page_title='Cartwheel | Resources', page_icon='🤸',initial_sidebar_state="collapsed")

# Move this initialization before the option_menu
#if "selected" not in st.session_state:
#   st.session_state.selected = "Documentation"

selected = option_menu(
   menu_title=None,  # No title to make it look like a navbar
   options=["Home", "Demo", "Resources", "Contact"],
   icons=["house", "book", "code", "people", "info"],  # Optional Bootstrap icons
   menu_icon="cast",
   default_index=2,
   orientation="horizontal",
)


# This initialization happens AFTER the menu selection
if "selected" not in st.session_state:
   st.session_state.selected = "Resources"
if selected != st.session_state.selected:
   st.session_state.selected = selected
   st.switch_page(f"pages/{selected.lower()}.py")
   # if selected == "Home":
   #     st.switch_page("pages/home.py")
   # else:
   #     st.switch_page(f"pages/{selected.lower()}.py")

# Documentation content
#st.title("Documentation", anchor=False)
st.markdown("<h1 style='text-align: center;'>Resources</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>.. in progress ..  </h3>", unsafe_allow_html=True)

