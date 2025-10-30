import requests
import json

uri = "http://localhost:11434/api/chat"

payload = {
    "model": "mistral",
    "messages": [
        {
            "role": "user",
            "content": "name a bollywood comedy movie with srk, just the name"
        }
    ],
    "stream": False  # disable streaming for simple blocking response
}

response = requests.post(uri, headers={"Content-Type": "application/json"}, json=payload)

data = response.json()

print(data)



# Step To Run PGM

# Step-1:   uv init
# Step-2:   uv venv
# Step-3:   .venv\Scripts\activate
# Step-4:   uv add requests
# Step-5:   python main.py