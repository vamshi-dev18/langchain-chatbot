from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Connect to OpenRouter using OpenAI-compatible format
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    openai_api_key=api_key,
    openai_api_base="https://openrouter.ai/api/v1"
)

# Memory to remember conversation history
memory = ConversationBufferMemory()

# Chain that connects LLM + Memory together
chatbot = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False
)

print("Chatbot ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chatbot.predict(input=user_input)
    print(f"Bot: {response}\n")