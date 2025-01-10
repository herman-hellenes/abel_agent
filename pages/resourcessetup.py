import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import json
import mypaths
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.row import row


# Keep the same navbar for consistency
st.set_page_config(layout='wide', page_title='Cartwheel | Demo Settings', page_icon='🤸',initial_sidebar_state="collapsed")

# Move this initialization before the option_menu
#if "selected" not in st.session_state:
#   st.session_state.selected = "Documentation"

selected = option_menu(
   menu_title=None,  # No title to make it look like a navbar
   options=["Home", "Logic Setup", "Resources Setup", "Evaluate", "Demo","Appointment"],
   icons=["house", "book", "code", "people", "info"],  # Optional Bootstrap icons
   menu_icon="cast",
   default_index=2,
   orientation="horizontal",
)


# This initialization happens AFTER the menu selection
if "selected" not in st.session_state:
   st.session_state.selected = "Resources Setup"
if selected != st.session_state.selected:
   st.session_state.selected = selected
   #st.switch_page(f"pages/{selected.lower().replace(" ","")}.py")
   st.switch_page(f"pages/{selected.lower().replace(' ', '')}.py")
   # if selected == "Home":
   #     st.switch_page("pages/home.py")
   # else:
   #     st.switch_page(f"pages/{selected.lower()}.py ")

st.markdown("<h1 style='text-align: center;'>Resources Setup </h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'> Selection of resources avaiable for the agent in the demonstration. This can be simply done in this manner by typing up the fields or integrated with APIs of choice straight to your system.  </h5>", unsafe_allow_html=True)
add_vertical_space(3)


st.markdown(" <h5> How to integrate chat agent into your website </h5>", unsafe_allow_html=True)
st.markdown("You simply add this to your React/HTML:", unsafe_allow_html=True)

code = '''<script src="<https://abelanalytics.com/agent/[your_company].js>" />
    '''
st.code(code, language="python")


st.markdown("Code example with curl to integrate your databases", unsafe_allow_html=True)

code = '''curl -s "https://api.example.com/get_inventory_data" | curl -X POST -H "Content-Type: application/json" -d @- "https://api.abelanalytics.com/post_inventory_data"
    '''
st.code(code, language="python")
# Start Prompt to bot
#################
st.markdown("<h3 style='text-align: center;'> Prompt Setup </h3>", unsafe_allow_html=True)

with open(mypaths.PERSONA, 'r') as file:
      content = file.read()

# Display the text content
st.text_area("Prompt Content", content, height=300) 
# Inventory
#################
st.markdown("<h3 style='text-align: center;'> Inventory </h3>", unsafe_allow_html=True)
print(mypaths.PERSONA)
print(mypaths.INVENTORY_FILE_PATH)
# Load the JSON data from the file
with open(mypaths.INVENTORY_FILE_PATH, 'r') as f:
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
st.markdown("<h3 style='text-align: center;'> FAQ </h3>", unsafe_allow_html=True)

# Load the JSON data from the file
with open(mypaths.FAQ_FILE_PATH, 'r') as f:
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




# customer database
#################
st.markdown("<h3 style='text-align: center;'> Customer Database </h3>", unsafe_allow_html=True)

# Load the JSON data from the file
with open(mypaths.CUSTOMER_DB_FILE_PATH, 'r') as f:
    data_customer = json.load(f)
df_customer= pd.DataFrame(data_customer) 
st.data_editor(df_customer, use_container_width=True)


# orders database
#################
st.markdown("<h3 style='text-align: center;'> Orders Database </h3>", unsafe_allow_html=True)

# Load the JSON data from the file
with open(mypaths.ORDERS_DB_FILE_PATH, 'r') as f:
    data_orders = json.load(f)
df_orders = pd.DataFrame(data_orders) 
st.data_editor(df_orders, use_container_width=True)




footer_html = """<div style='text-align: center;'>
  <p>Developed by herman@abelanalytics.no </p>
</div>"""


add_vertical_space(3)
st.markdown(footer_html, unsafe_allow_html=True)
logo = "public/abel-analytics-high-resolution-logo-transparent (1).png"
with st.columns(3)[1]:
    st.image(logo)


# links_row = row(1, vertical_align="center")
# links_row.button(
#     "✉️   herman@abelanalytics.no ",
#     "herman@abelanalytics.no",
#     use_container_width=True,
# )

