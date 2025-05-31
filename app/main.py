import streamlit as st
from src.chatbot.rag_chatbot import ChatBot

st.set_page_config(page_title="Customer Support Chatbot")
st.title("📘 Customer Support RAG Chatbot")

bot = ChatBot()

query = st.text_input("Ask your question:")

if query:
    with st.spinner("Thinking..."):
        answer = bot.chat(query)
        st.markdown(f"**Answer:** {answer}")
