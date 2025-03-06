import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv() # load environments variables from .env project file

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)