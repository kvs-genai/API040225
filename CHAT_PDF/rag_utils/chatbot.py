from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

def ask_question(client, query, collection_name):
    collection = client.get_or_create_collection(name=collection_name)
    results = collection.query(query_texts=[query],n_results=10)

    if not results or not results["documents"]:
        return "I don't know"
    system_prompt = f"""
    You are a helpful assistant. Answer the questions based only on the provided data and do not use your
    knowledge

    Question: {query}
    Data: {str(results['documents'])}

    If you do not know the answers reply with I don't know only
    """

    chatbot_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = chatbot_client.chat.completions.create(
        messages=[
            {"role":"system", "content": system_prompt},
            {"role": "user", "content": "query"}
        ],
        model = "llama3-8b-8192",
        temperature = 0
    )

    return response.choices[0].message.content
