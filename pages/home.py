import streamlit as st
from streamlit_option_menu import option_menu
# Keep the same navbar for consistency
st.set_page_config(layout='wide', page_title='Cartwheel | GenAI in the workforce', page_icon='🤸',initial_sidebar_state="collapsed")

# Move this initialization before the option_menu
#if "selected" not in st.session_state:
#   st.session_state.selected = "Documentation"

selected = option_menu(
   menu_title=None,  # No title to make it look like a navbar
   options=["Home", "LogicSetup", "ResourcesSetup", "Demo"],
   icons=["house", "book", "code", "people", "info"],  # Optional Bootstrap icons
   menu_icon="cast",
   default_index=0,
   orientation="horizontal",
)


# This initialization happens AFTER the menu selection
if "selected" not in st.session_state:
   st.session_state.selected = "Home"
if selected != st.session_state.selected:
   st.session_state.selected = selected
   st.switch_page(f"pages/{selected.lower()}.py")
   # if selected == "Home":
   #     st.switch_page("pages/home.py")
   # else:
   #     st.switch_page(f"pages/{selected.lower()}.py")


#logo = "public/abel-analytics-high-resolution-logo.png"
logo = "public/abel-analytics-high-resolution-logo-transparent (1).png"
with st.columns(3)[1]:
    st.image(logo)

# Header

st.markdown("<h1 style='text-align: center;'>AI Agents that actually complete work</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>We power up advanced AI agents with complex reasoning and problem-solving skills. You can integrate everywhere and give them tools and context to do the job. </h3>", unsafe_allow_html=True)



import streamlit_extras
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.row import row



add_vertical_space(1)
#st.markdown("#### Learn more")
links_row = row(4, vertical_align="center")
links_row.button(
    "🕐   Everywhere - All at Once",
    use_container_width=True,
)
links_row.button(
    "🐙   Live&Log Monitoring",
    #"https://github.com/arnaudmiribel/streamlit-extras",
    use_container_width=True,
)
links_row.button(
    "🔑   Integrate Anywhere",
    #"https://github.com/arnaudmiribel/streamlit-extras",
    use_container_width=True,
)
links_row.button(
    "🔖  100+ languages",
    #"https://github.com/arnaudmiribel/streamlit-extras",
    use_container_width=True,
)
links_row = row(4, vertical_align="center")
links_row.button(
    "🤚   Human Live Escalation ",
    use_container_width=True,
)
links_row.button(
    "🤗   Setting personality & memory",
    #"https://github.com/arnaudmiribel/streamlit-extras",
    use_container_width=True,
)
links_row.button(
    "🤖   openAI, Anthropic, Llama, Groc",
    #"https://github.com/arnaudmiribel/streamlit-extras",
    use_container_width=True,
)
links_row.button(
    "🔧   Tools ",
    #"https://github.com/arnaudmiribel/streamlit-extras",
    use_container_width=True,
)

add_vertical_space(1)

st.markdown("<h5 > Imagine a customer facing AI that can actually </h5>", unsafe_allow_html=True)



st.markdown("- carry out a booking")
st.markdown("- purchase")
st.markdown("- customer authentication")
st.markdown("- send emails")
st.markdown("- send emails")

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)

st.markdown(".. to let you and your customers be as productive as possible."
    "One agent can serve online customer support, another serve in the internal HR team, while another at IT support. "
    ,
    unsafe_allow_html=True
)

#st.code(body, language="python", *, line_numbers=False, wrap_lines=False)


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
