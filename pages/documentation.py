import streamlit as st
from streamlit_option_menu import option_menu
# Keep the same navbar for consistency
st.set_page_config(layout='wide', page_title='Cartwheel | GenAI in the workforce', page_icon='🤸',initial_sidebar_state="collapsed")

# Move this initialization before the option_menu
#if "selected" not in st.session_state:
#   st.session_state.selected = "Documentation"

selected = option_menu(
   menu_title=None,
   options=["Home", "Documentation", "Examples", "Community", "About"],
   icons=["house", "book", "code", "people", "info"],
   menu_icon="cast",
   default_index=1,  # Documentation is selected by default
   orientation="horizontal",
   key="nav" 
)

# This initialization happens AFTER the menu selection
if "selected" not in st.session_state:
   st.session_state.selected = "Documentation"
if selected != st.session_state.selected:
   st.session_state.selected = selected
   st.switch_page(f"pages/{selected.lower()}.py")
   # if selected == "Home":
   #     st.switch_page("pages/home.py")
   # else:
   #     st.switch_page(f"pages/{selected.lower()}.py")

# Documentation content
#st.title("Documentation", anchor=False)
st.markdown("<h1 style='text-align: center;'>AI Agents that actually complete work</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>We power up advanced AI agents with complex reasoning and problem-solving skills. You can integrate everywhere and give them tools to do the job. </h3>", unsafe_allow_html=True)



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

st.markdown(
    "Imagine a customer facing AI that can actually carry out a booking, "
    "a purchase, authentication, send emails, answer questions, "
    "to let you and your customers be as productive as possible."
    "One agent can serve online customer support, another serve in the internal HR team, while another at IT support. "
    ,
    unsafe_allow_html=True
)


#st.code(body, language="python", *, line_numbers=False, wrap_lines=False)

