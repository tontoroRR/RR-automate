import os
from dotenv import load_dotenv
from notion_client import Client

load_dotenv(verbose=True)
load_dotenv('.env')

token = os.environ.get('notion_api_key')



