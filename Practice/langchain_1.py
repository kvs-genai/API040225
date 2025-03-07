import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = init_chat_model(model_name = "gpt-4o-mini", model_provider = "openai")

messages = [
    SystemMessage(content="Act sircastically"),
    HumanMessage(content="I am Ramesh")
]

respsonse = model.invoke(messages)

print(response)