# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv("GROQ_API_KEY")

# # This is EXACTLY what the Groq library does under the hood
# url = "https://api.groq.com/openai/v1/chat/completions"

# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }

# body = {
#     "model": "llama-3.3-70b-versatile",
#     "messages": [
#         {"role": "system", "content": "You are MAX, Shubham's personal AI friend."},
#         {"role": "user", "content": "Give me one tip to lose belly fat. Keep it short."}
#     ],
#     "max_tokens": 150
# }

# response = requests.post(url, headers=headers, json=body)

# # print("STATUS CODE:", response.status_code)
# # print("RAW RESPONSE:")
# # print(response.json())

# data = response.json()
# message = data["choices"][0]["message"]["content"]
# print("\nMAX SAYS:", message)

# # Change your api_key line to this temporarily
# api_key = "fake-key-123"

# response = requests.post(url, headers=headers, json=body)
# print("Status code:", response.status_code)   # Will show 401
# print(response.json())                         # Will show error message

import requests
import os
from dotenv import load_dotenv

load_dotenv()

def call_groq(message):
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        return "Error: No API key found"
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    body = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "You are MAX, Shubham's AI friend. Be direct and brief."},
            {"role": "user", "content": message}
        ],
        "max_tokens": 200
    }
    
    try:
        response = requests.post(url, headers=headers, json=body)
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error {response.status_code}: {response.json()}"
            
    except Exception as e:
        return f"Something went wrong: {e}"


# Test it with 3 different questions
questions = [
    "Give me one tip to lose belly fat",
    "What should I learn after Python?",
    "How many hours should I sleep to build muscle?"
]

for question in questions:
    print(f"Shubham: {question}")
    print(f"MAX: {call_groq(question)}")
    print("---")