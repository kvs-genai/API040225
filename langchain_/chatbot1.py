import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = init_chat_model("llama3-8b-8192", model_provider="groq")
messages = [
    SystemMessage(content="Act sarcastically"),
    HumanMessage(content="I am Ramesh")
    ]

res = model.invoke(messages)

print(res.content)