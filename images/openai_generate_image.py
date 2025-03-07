import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=openai_api_key
)

response = client.images.generate(
    model="dall-e-3",
    prompt="a beautiful house sorrounded by long trees and a lake",
    size="1024x1024",
    quality="standard",
    n=1,
)

print(response.data[0].url)