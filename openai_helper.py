from dotenv import load_dotenv
import os
import openai
import json

load_dotenv()
api_key = os.getenv("openai_key")
openai.api_key = api_key