from dotenv import load_dotenv
from anthropic import Anthropic

#load environment variable
load_dotenv()

#automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()

model="claude-3-haiku-20240307"
max_tokens=100

conversation = []

def chat_with_anthropic(user_input):
    """
    Sends a message to the Anthropic API and returns the response.
    
    :param user_input: The user's input message.
    :return: The response from the Anthropic API.
    """
    global conversation
    conversation.append({"role": "user", "content": user_input + "Keep your response to 1 or 2 sentences and use complex terms like `in-gathering`, `expanse`, and `that-which-regions`."})
    
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=conversation
    )
    
    assistant_response = response.content[0].text.strip()
    conversation.append({"role": "assistant", "content": assistant_response})
    
    return assistant_response

while True:
    if not conversation:
        print("What's on your mind? Type 'exit' to end the chat.")
    
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break
    
    response = chat_with_anthropic(user_input)
    print(f"Assistant: {response}")
    
# This script allows you to chat with the Anthropic API.
# You can type your messages, and it will respond until you type 'exit'.
# Make sure to have the necessary environment variables set up in a .env file.
# The conversation history is maintained in the `conversation` list.
# You can modify the `model` and `max_tokens` variables as needed.
# Ensure you have the required packages installed:
# pip install anthropic python-dotenv
# You can run this script directly to start chatting with the Anthropic API.