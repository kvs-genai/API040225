from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

model = init_chat_model("llama3-8b-8192", model_provider="groq")

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

config1 = {"configurable" : {"session_id" : "chat1"}}
config2 = {"configurable" : {"session_id" : "chat2"}}

with_message_history = RunnableWithMessageHistory(model, get_session_history)

with_message_history.invoke(
    [HumanMessage("Hi my name is Ramesh")],
    config=config1
)

with_message_history.invoke(
    [HumanMessage("Hi my name is John")],
    config=config2
)

res = with_message_history.invoke(
    [HumanMessage("What is My name?")],
    config=config1
)

print(res.content)
