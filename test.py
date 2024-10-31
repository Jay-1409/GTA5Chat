import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv()
print(os.getenv("API_key"))