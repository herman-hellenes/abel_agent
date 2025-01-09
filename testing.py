from dotenv import load_dotenv
import os
load_dotenv()  # load environment variables from .env file
PERSONA = os.getenv('PERSONA')

with open("resources/"+PERSONA+"/prompt.txt", 'r') as file:
      content = file.read()

print(content)      