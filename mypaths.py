AGENT_TYPE = 'flower_shop' #must correspond to subfolder of ./resources
#Setting the Resources
PERSONA = 'resources/'+AGENT_TYPE+'/prompt.txt'
GREETING = 'resources/'+AGENT_TYPE+'/greeting.txt'
FAQ_FILE_PATH = 'resources/'+AGENT_TYPE+'/FAQ.json'
INVENTORY_FILE_PATH = 'resources/'+AGENT_TYPE+'/inventory.json'
EVALUATION_FILE_PATH = 'resources/'+AGENT_TYPE+'/evaluation.json'
CUSTOMER_DB_FILE_PATH = 'resources/'+AGENT_TYPE+'/customers_database.json'
ORDERS_DB_FILE_PATH = 'resources/'+AGENT_TYPE+'/orders_database.json'

DB_PATH = './.chroma_db' #might edit this to each use case?!?!