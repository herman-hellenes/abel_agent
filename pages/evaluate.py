import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import json
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.row import row
import mypaths
# Keep the same navbar for consistency
st.set_page_config(layout='wide', page_title='Cartwheel | Evaluate', page_icon='🤸',initial_sidebar_state="collapsed")

# Move this initialization before the option_menu
#if "selected" not in st.session_state:
#   st.session_state.selected = "Documentation"

selected = option_menu(
   menu_title=None,  # No title to make it look like a navbar
   options=["Home", "Logic Setup", "Resources Setup", "Evaluate", "Demo","Appointment"],
   icons=["house", "book", "code", "people", "info"],  # Optional Bootstrap icons
   menu_icon="cast",
   default_index=3,
   orientation="horizontal",
)


# This initialization happens AFTER the menu selection
if "selected" not in st.session_state:
   st.session_state.selected = "Evaluate"
if selected != st.session_state.selected:
   st.session_state.selected = selected
   #st.switch_page(f"pages/{selected.lower()}.py")
   st.switch_page(f"pages/{selected.lower().replace(' ', '')}.py")
   # if selected == "Home":
   #     st.switch_page("pages/home.py")
   # else:
   #     st.switch_page(f"pages/{selected.lower()}.py")

st.markdown("<h1 style='text-align: center;'>Evaluation and monitoring </h1>", unsafe_allow_html=True)

st.markdown("""<h6 style='text-align: center;'> We offer three distinct methods of evaluating an agent. Evaluations are run automatically 
            when any change is done, or on-demand. Typically you would run through evaluations if the prompt setup is changed, you try out another LLM provider, etc. 
             </h6>""", unsafe_allow_html=True)


links_row = row(3, vertical_align="center")
links_row.button(
    "📱Automated Benchmarking",
    use_container_width=True,
)
links_row.button(
    "🧍   Humans as judges",
    #"https://github.com/arnaudmiribel/streamlit-extras",
    use_container_width=True,
)
links_row.button(
    "🤖   LLMs as judges",
    #"https://github.com/arnaudmiribel/streamlit-extras",
    use_container_width=True,
)

st.markdown("<h3 >Evaluation </h3>", unsafe_allow_html=True)

# Q&A to bot
#################
#st.markdown("<h4 style='text-align: center;'> FAQ </h4>", unsafe_allow_html=True)

# Load the JSON data from the file
st.markdown("For each model run, such overview is available:", unsafe_allow_html=True)

with open(mypaths.EVALUATION_FILE_PATH, 'r') as f:
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

st.markdown("Collection of all runs are stored and can be reverted to. Thus one can see test performance as before setting out a new agent config in production.", unsafe_allow_html=True)
df = pd.DataFrame(
    [
        {"LLM":" openai:gpt-4o", "LLJudgeScore" : 8.4, "HumanJudgeScore" : 7.3, "DeployDate": "2024-10-10"},
        {"LLM": "openai:o1-mini", "LLJudgeScore" : 9.4, "HumanJudgeScore" : 8.3,"DeployDate": "2024-11-15"},
        {"LLM": "openai:gpt-4-turbo", "LLJudgeScore" : 9.5, "HumanJudgeScore" : 9,"DeployDate": "2024-12-15"},
    ]
)
df.index.name = 'ModelID'
st.dataframe(df, use_container_width=True)

st.markdown("<h3 > Monitoring </h3>", unsafe_allow_html=True)
st.markdown("Montitoring is done live and recorded in databases, measuring number of conversations, customer satisfaction, question resolution and ROI.")  # H3 header

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("# Conversations / week ", "151 221", "2 %", border=True)
b.metric("Resolution %", "70 % ", "2 %", border=True)

c.metric("ROI", "91%", "5%", border=True)
d.metric("Satisfaction", "85 %", "8 %", border=True)

from datetime import datetime, timedelta

# Create date range for the last month
end_date = datetime.now()
start_date = end_date - timedelta(days=30)
dates = pd.date_range(start=start_date, end=end_date, freq='D')
import numpy as np

# Create random values between 1 and 10
linear_trend = np.linspace(10000, 151221, len(dates))
noise = np.random.normal(0, 5000, len(dates))
values = np.clip(linear_trend + noise, 1, 151221)

# Create DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Value': values.round(2)
})

# Set Date as index (optional)
#df.set_index('Date', inplace=True)
#st.subheader("Monthly Performance Metrics")
st.markdown("#### Conversations / week")  # H3 header

st.line_chart(
    df,
    x="Date",
    y="Value",
    color=["#FF0000"],  # Optional
)

st.markdown("#### Topics of the week")  # H3 header

topic_data = {
    'Topic': [
        'Account Issues',
        'Delivery Status', 
        'Payment Problems',
        'Pricing', 
        
        'Returns', 
        'Technical Support'
        
    ],
    'Count': [72021, 62021, 32021, 12021, 2021, 1021]
}

# Create DataFrame
df = pd.DataFrame(topic_data)
df = df.sort_values('Count', ascending=False)
st.bar_chart(
    df.set_index('Topic')  # Set Topic as index for the chart
    ,horizontal=True
)

#FOOTER
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


# links_row = row(1, vertical_align="center")
# links_row.button(
#     "✉️   herman@abelanalytics.no ",
#     "herman@abelanalytics.no",
#     use_container_width=True,
# )

