import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

uri = "https://api.openai.com/v1/chat/completions"

api_key=os.getenv("OPENAI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "gpt-4o",
    "messages": [
        {
            "role": "user",
            "content": "name a bollywood comedy movie with srk, just the name"
        }
    ]
}

response = requests.post(uri, headers=headers, json=payload)
print(response.json())