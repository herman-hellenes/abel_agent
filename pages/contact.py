import streamlit as st
from streamlit_option_menu import option_menu
# Keep the same navbar for consistency
st.set_page_config(layout='wide', page_title='Cartwheel | Contact', page_icon='🤸',initial_sidebar_state="collapsed")

# Move this initialization before the option_menu
#if "selected" not in st.session_state:
#   st.session_state.selected = "Documentation"

selected = option_menu(
   menu_title=None,  # No title to make it look like a navbar
   options=["Home", "LogicSetup", "ResourcesSetup", "Contact"],
   icons=["house", "book", "code", "people", "info"],  # Optional Bootstrap icons
   menu_icon="cast",
   default_index=3,
   orientation="horizontal",
)


# This initialization happens AFTER the menu selection
if "selected" not in st.session_state:
   st.session_state.selected = "Contact"
if selected != st.session_state.selected:
   st.session_state.selected = selected
   st.switch_page(f"pages/{selected.lower()}.py")
   # if selected == "Home":
   #     st.switch_page("pages/home.py")
   # else:
   #     st.switch_page(f"pages/{selected.lower()}.py")

# Documentation content
#st.title("Documentation", anchor=False)
st.markdown("<h1 style='text-align: center;'>Get in touch</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'> herman@abelanalytics.no </h3>", unsafe_allow_html=True)


# Footer
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.row import row
footer_html = """<div style='text-align: center;'>
  <p>Developed with ❤️ by </p>
</div>"""


add_vertical_space(3)
st.markdown(footer_html, unsafe_allow_html=True)
logo = "public/abel-analytics-high-resolution-logo-transparent (1).png"
with st.columns(3)[1]:
    st.image(logo)

links_row = row(1, vertical_align="center")
links_row.button(
    "✉️   herman@abelanalytics.no ",
    "herman@abelanalytics.no",
    use_container_width=True,
)



