import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.row import row
# Keep the same navbar for consistency
st.set_page_config(layout='wide', page_title='Cartwheel | LogicSetup', page_icon='🤸',initial_sidebar_state="collapsed")

# Move this initialization before the option_menu
#if "selected" not in st.session_state:
#   st.session_state.selected = "Documentation"

selected = option_menu(
   menu_title=None,  # No title to make it look like a navbar
   options=["Home", "Logic Setup", "Resources Setup","Evaluate", "Demo","Appointment"],
   icons=["house", "book", "code", "people", "info"],  # Optional Bootstrap icons
   menu_icon="cast",
   default_index=1,
   orientation="horizontal",
)


# This initialization happens AFTER the menu selection
if "selected" not in st.session_state:
   st.session_state.selected = "logic setup"
if selected != st.session_state.selected:
   st.session_state.selected = selected
   #st.switch_page(f"pages/{selected.lower()}.py")
   st.switch_page(f"pages/{selected.lower().replace(' ', '')}.py")
   # if selected == "Home":
   #     st.switch_page("pages/home.py")
   # else:
   #     st.switch_page(f"pages/{selected.lower()}.py")

# Documentation content
#st.title("Documentation", anchor=False)
st.markdown("<h1 style='text-align: center;'>Logic Setup </h1>", unsafe_allow_html=True)

option = st.selectbox(
    "Select LLM ",
    ("openai:gpt-4o", "openai:o1-mini", "openai:gpt-4-turbo","anthropic:claude-3-5-sonnet-20240620","anthropic:claude-3-5-haiku-20241022","google:gemini-2.0-flash-exp",
     "together:meta-llama/Llama-3.3-70B-Instruct-Turbo","groq:llama-3.3-70b-versatile","perplexity:llama-3.1-sonar-huge-128k-online"),
)

st.write("You selected:", option)

st.markdown("<h6 style='text-align: left;'> Further setup of workflow and interaction of tooling; below is the current example that's applied in the Demo. In logged in pages, this is interactive with numerous templates and customization. </h6>", unsafe_allow_html=True)


st.image("https://github.com/user-attachments/assets/62305fcb-3414-41a2-9e2d-8f306219ccc0")


from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.row import row
footer_html = """<div style='text-align: center;'>
  <p>Developed by herman@abelanalytics.no </p>
</div>"""


add_vertical_space(3)
st.markdown(footer_html, unsafe_allow_html=True)
logo = "public/abel-analytics-high-resolution-logo-transparent (1).png"
with st.columns(3)[1]:
    st.image(logo)
