AGENT_TYPE = 'xc_sport' #must correspond to subfolder of ./resources

#TRY TO GET THIS UPDATED DYNAMICALLY
# import streamlit as st
# def get_agent_config():
#    # Always get the latest value from session state
#    return {
#        "agent_type": st.session_state.get('AGENT_TYPE', 'xc_sport'),
#        "path": f"path/to/{st.session_state.get('AGENT_TYPE', 'General').lower()}"
#    }
# # Use it when needed
# config = get_agent_config()
# AGENT_TYPE = config['agent_type']
#GENT_PATH = config['path']

#Setting the Resources
PERSONA = 'resources/'+AGENT_TYPE+'/prompt.txt'
GREETING = 'resources/'+AGENT_TYPE+'/greeting.txt'
FAQ_FILE_PATH = 'resources/'+AGENT_TYPE+'/FAQ.json'
INVENTORY_FILE_PATH = 'resources/'+AGENT_TYPE+'/inventory.json'
EVALUATION_FILE_PATH = 'resources/'+AGENT_TYPE+'/evaluation.json'
CUSTOMER_DB_FILE_PATH = 'resources/'+AGENT_TYPE+'/customers_database.json'
ORDERS_DB_FILE_PATH = 'resources/'+AGENT_TYPE+'/orders_database.json'
DB_PATH = './resources/'+AGENT_TYPE+'/.chroma_db' #might edit this to each use case?!?!

#DB_PATH = './.chroma_db' #might edit this to each use case?!?!