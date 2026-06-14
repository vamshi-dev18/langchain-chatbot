from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import streamlit as st
import os

# Load API key
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Page config
st.set_page_config(page_title="My Chatbot", page_icon="🤖")
st.title("🤖 My AI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize LLM
if "llm" not in st.session_state:
    st.session_state.llm = ChatOpenAI(
        model="openai/gpt-3.5-turbo",
        openai_api_key=api_key,
        openai_api_base="https://openrouter.ai/api/v1"
    )

# Display chat history
for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.write(msg.content)

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # Get response with full history
    response = st.session_state.llm.invoke(st.session_state.messages)

    # Add bot response
    st.session_state.messages.append(AIMessage(content=response.content))
    with st.chat_message("assistant"):
        st.write(response.content)