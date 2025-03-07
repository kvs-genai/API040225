import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)

chat_completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                max_completion_tokens=1024,
                top_p=1,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant"
                    },
                    {
                        "role": "user",
                        "content":"Explain the importance of fast language models"
                    }
                ]
            )

print(chat_completion.choices[0].message.content)