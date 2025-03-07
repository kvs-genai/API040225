import os
from dotenv import load_dotenv
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.gemini import Gemini
from llama_index.core import Settings
from llama_index.core import SimpleDirectoryReader

load_dotenv()

#print(os.getenv("GOOGLE_API_KEY"))

Settings.embed_model = HuggingFaceEmbedding(model_name = "sentence-transformers/all-MiniLM-L6-v2")
Settings.llm = Gemini(model_name = "models/gemini-pro", api_key=os.getenv("GOOGLE_API_KEY"))

documents = SimpleDirectoryReader(input_dir="docs").load_data()
#print(documents)

from llama_index.core.node_parser import SentenceSplitter
text_splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)
Settings.text_splitter = text_splitter

from llama_index.core import VectorStoreIndex
index = VectorStoreIndex.from_documents(documents,transformations=[text_splitter])

#index.storage_context.persist(persist_dir="./ParseDB")
index.storage_context.persist()   # creates default storage folder

from llama_index.core import StorageContext, load_index_from_storage

storage_context = StorageContext.from_defaults(persist_dir="./storage")

index = load_index_from_storage(storage_context)


template = """"
You are a knoweldeable assistant specialized in answering questions.
Your goal is to provide accurate, concise relevant answers.

Here is the question and context
\nQuestion: {question} \ncontext: {context} \Answer: 
"""

from llama_index.core.prompts import PromptTemplate

prompt_tmpl = PromptTemplate(
    template = template,
    template_var_mappings={"query_str" : "question", "context_str" : "context"}
)

from llama_index.core import get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine


retriever = VectorIndexRetriever(
    index = index,
    similarity_top_k=10
)

response_senthesizer = get_response_synthesizer()

query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_senthesizer
)

query_engine.update_prompts(
    {"response_synthesizer:text_qa_template" : prompt_tmpl }
)

response = query_engine.query("what is Generative AI")
print(response)