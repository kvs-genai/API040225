import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.images.generate(
    model = "dall-e-3",
    prompt = "A giant chasing Jack",
    size = "1024x1024",
    quality = "standard",
    n=1
)
print(response.data[0].url)