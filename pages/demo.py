import streamlit as st
from vector_store import FlowerShopVectorStore
from chatbot import app
from langchain_core.messages import AIMessage, HumanMessage
from tools import customers_database, data_protection_checks
from streamlit_extras.add_vertical_space import add_vertical_space





#from streamlit_navigation_bar import st_navbar

st.set_page_config(layout='wide', page_title='Cartwheel | Everlyn Demo', page_icon='🤸',initial_sidebar_state="collapsed" )

#Navbar
from streamlit_option_menu import option_menu
selected = option_menu(
   menu_title=None,  # No title to make it look like a navbar
   options=["Home", "LogicSetup", "ResourcesSetup", "Evaluate","Demo"],
   icons=["house", "book", "code", "people", "info"],  # Optional Bootstrap icons
   menu_icon="cast",
   default_index=4,
   orientation="horizontal",
)

if "selected" not in st.session_state:
   st.session_state.selected = "Demo"
if selected != st.session_state.selected:
   st.session_state.selected = selected
   st.switch_page(f"pages/{selected.lower()}.py")

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
#st.write(f"You selected {selected}")
# Handle navigation


st.markdown("<h1 style='text-align: center;'>  🧘‍♀️ Everlyn, the flower shop agent</h1>", unsafe_allow_html=True)

st.markdown("This is a live demo of the interaction with an agent that can answer your questions, tips of what to buy, create new orders and update the relevant databases and review existing orders. We here display way more than what an end-user will see; including the agent's chain of thought in order to come up with the final answer, the customer database on the top right, and below that the data protection checks.", unsafe_allow_html=True)
st.page_link("pages/resourcessetup.py", label="To review and edit resources", icon="🪛")
st.page_link("pages/logicsetup.py", label="To review and edit logic", icon="🔨")


add_vertical_space(1)



if 'message_history' not in st.session_state:
    st.session_state.message_history = [AIMessage(content="Hiya, I'm Everlyn, the flower shop chatbot. How can I help?")]

left_col, main_col, right_col = st.columns([1, 2, 1])

# 1. Buttons for chat - Clear Button

with left_col:
    if st.button('Clear Chat'):
        st.session_state.message_history = []


# 2. Chat history and input
with main_col:
    user_input = st.chat_input("Type here...")

    if user_input:
        st.session_state.message_history.append(HumanMessage(content=user_input))

        response = app.invoke({
            'messages': st.session_state.message_history
        })

        st.session_state.message_history = response['messages']

    for i in range(1, len(st.session_state.message_history) + 1):
        this_message = st.session_state.message_history[-i]
        if isinstance(this_message, AIMessage):
            message_box = st.chat_message('assistant')
        else:
            message_box = st.chat_message('user')
        message_box.markdown(this_message.content)
# 3. State variables

with right_col:
    st.title('customers database')
    st.write(customers_database)
    st.title('data protection checks')
    st.write(data_protection_checks)




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


