from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import streamlit as st
import os

# Load API key
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Page config
st.set_page_config(page_title="My Chatbot", page_icon="🤖")
st.title("🤖 My AI Chatbot")

# Initialize memory and chain once per session
if "chatbot" not in st.session_state:
    llm = ChatOpenAI(
        model="openai/gpt-3.5-turbo",
        openai_api_key=api_key,
        openai_api_base="https://openrouter.ai/api/v1"
    )
    memory = ConversationBufferMemory()
    st.session_state.chatbot = ConversationChain(llm=llm, memory=memory)
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Get bot response
    response = st.session_state.chatbot.predict(input=user_input)

    # Show bot response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)