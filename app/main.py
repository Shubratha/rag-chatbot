import os
import streamlit as st
import sys
from src.chatbot.rag_chatbot import ChatBot

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

st.set_page_config(page_title="Customer Support Chatbot")
st.title("📘 Customer Support RAG Chatbot")

bot = ChatBot()

query = st.text_input("Ask your question:")

if query:
    with st.spinner("Thinking..."):
        answer = bot.chat(query)
        st.markdown(f"**Answer:** {answer}")
