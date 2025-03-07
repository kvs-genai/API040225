import os
import streamlit as st
from rag_utils.pdf_handler import handle_pdf_upload
from rag_utils.chunk_handler import process_pdf
from rag_utils.chormadb_client import chroma_insert_documents, get_chroma_client
from rag_utils.chatbot import ask_question

# Setup page
st.set_page_config(page_title="RAGA")
st.title("RAG PDF Chatbot")

# Sidebar
st.sidebar.header("Upload PDF")
uploaded_files = st.sidebar.file_uploader("Choose pdf files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    st.sidebar.success(f"Uploaded {len(uploaded_files)} file(s)")
    save_folder = "docs"
    os.makedirs(save_folder, exist_ok=True)

    # Handle uploads
    saved_files = handle_pdf_upload(uploaded_files, save_folder)
    st.sidebar.success("File saved successfully")

# Button to process pdf

if st.button("Process uploaded pdf"):
    if uploaded_files:
        st.info("Processing documents")
        raw_docs = process_pdf("docs")
        chroma_client = get_chroma_client(path="CHAT_PDF/chroma_db")
        chroma_insert_documents(client=chroma_client, collection_name="ai_docs", documents=raw_docs)
        st.success("Document processed successfully")
        st.write(raw_docs)
    else:
        st.warning("Please upload pdf")

st.header("Ask your question")

user_query = st.text_input("", placeholder="Enter your question")

if user_query:
    chroma_client = get_chroma_client(pat="CHAT_PDF/chroma-db")
    response = ask_question(chroma_client, user_query, collection_name="ai_docs")
    st.subheader("Chatbot Response")
    st.write(response)