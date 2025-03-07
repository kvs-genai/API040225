import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")
client = Groq(
    api_key=groq_api_key
)

st.header("Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []


# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

def chatbot_response(user_msg):
    st.write(st.session_state.messages)
    chat_completion = client.chat.completions.create(
    model="deepseek-r1-distill-llama-70b",
    messages=st.session_state.messages
    )
    return chat_completion.choices[0].message.content

user_msg = st.chat_input("Enter your message")
response = ""

if user_msg:
    st.session_state.messages.append({"role":"user", "content":user_msg})
    with st.chat_message("user"):
        st.write(user_msg)
    with st.chat_message("assistant"):
        response = chatbot_response(user_msg)
        st.write(response)    
    st.session_state.messages.append({"role":"assistant","content": response})

