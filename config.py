import os
import json

def initialize_config():
    file_name = 'config.json'
    with open(file_name, 'r') as file:
        config = json.load(file)
        os.environ['OPENAI_API_KEY'] = config.get("API_KEY") # Loading the API Key
        os.environ["OPENAI_BASE_URL"] = config.get("OPENAI_API_BASE") # Loading the API Base Url

    base = os.environ["OPENAI_BASE_URL"]
    key = os.environ['OPENAI_API_KEY']

    return base,key
