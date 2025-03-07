import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {
            "role": "developer",
            "content" : "Act as helpful assistant"
        },
        {
            "role" : "user",
            "content" : "Write 100 words about AI"
        }
    ],
    stream = True
)

for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
#print(response.choices[0].message.content)