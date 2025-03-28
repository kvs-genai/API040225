import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
# print(api_key)

client = OpenAI(
    api_key=openai_api_key
)


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "developer", 
            "content": "You are a helpful assistant."
         },
        {
            "role": "user",
            "content": "Write 100 words about AI"
        }
    ]
)


print(completion.choices[0].message.content)