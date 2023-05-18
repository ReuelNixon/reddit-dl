import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
user_agent = os.environ.get("USER_AGENT")
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
