import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model # initializes the model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
# print(groq_api_key)

model = init_chat_model("deepseek-r1-distill-llama-70b", model_provider="groq")

# messages= [
#     SystemMessage("Translate the following from English to Hindi"),
#     HumanMessage("How are you")
# ]

# result = model.invoke(messages)
# print(result)

system_template = "Translate the following from english to {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", "{text}")
    ]
)

prompt = prompt_template.invoke({"language" : "telugu", "text" : "how are you?"})
response = model.invoke(prompt)
print(response.content)