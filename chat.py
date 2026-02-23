import os  # Helps Python interact with your computer's operating system
from groq import Groq  # The official library to talk to Groq's AI models
from dotenv import load_dotenv  # Tool to read secret keys from a .env file

# 1. SETUP: Load your secret API key into the script's memory
load_dotenv() 

# 2. INITIALIZATION: Create the 'client' using your secret key from the .env file
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 3. MEMORY: An empty list to store the chat history so MAX doesn't forget context
conversation_history = []

# 4. PERSONALITY: The instructions that tell the AI how to behave and who it is
system_prompt = """You are MAX, Shubham's personal AI friend. 
You are warm, direct, and brutally honest.
You help Shubham with fitness, career, diet, grooming, finance, and daily life.
You remember everything he tells you within this conversation.
Talk like a smart friend, not a textbook.
Always push Shubham to be better — but with respect."""

# 5. UI: Greeting messages shown when the program starts
print("MAX: Hey Shubham! I'm MAX, your personal AI friend.")
print("MAX: Tell me anything — fitness, career, life. I'm here.")
print("(type 'quit' to exit)\n")

# 6. THE LOOP: This keeps the program running for a back-and-forth conversation
while True:
    # Get input from you (Shubham) via the terminal
    user_input = input("Shubham: ")

    # Exit condition: If you type 'quit', the loop stops and the program ends
    if user_input.lower() == 'quit':
        print("MAX: See you tomorrow. Stay consistent. 💪")
        break

    # Add your message to the 'memory' list
    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    # 7. THE REQUEST: Send the prompt and history to Groq's servers
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", # The specific 'brain' being used
        messages=[
            {"role": "system", "content": system_prompt}, # Give personality first
            *conversation_history # Unpack and send the whole chat history
        ],
        max_tokens=1024 # Limit the length of the AI's response
    )

    # 8. EXTRACTION: Dig into the 'response' object to get the actual text reply
    assistant_message = response.choices[0].message.content

    # Save MAX's reply to the 'memory' so it's remembered in the next turn
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    # 9. OUTPUT: Print MAX's response to the terminal
    print(f"\nMAX: {assistant_message}\n")