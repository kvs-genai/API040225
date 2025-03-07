import chromadb

import os
import streamlit as st
from time import sleep

def get_chroma_client(path):
    """"
    Return a persistent ChromaDB
"""
    return chromadb.PersistentClient(path=path)

def chroma_insert_documents(client, collection_name, documents):
    collection = client.get_or_create_collection(name=collection_name)

    docs, metadata, ids = [], [] ,[]

    for i, chunk in enumerate(documents):
        docs.append(chunk.page_content)
        metadata.append(chunk.metadata)
        ids.append(f"ID{i}")
    
    collection.upsert(
        documents = docs,
        metadatas = metadata,
        ids = ids
    )
    