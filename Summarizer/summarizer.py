import os
from dotenv import load_dotenv
import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

load_dotenv()

st.set_page_config(page_title="Scrapper Summarizer")
st.title("Scrapper Summarizer")
st.subheader("Summarize your youtube or any url")

url = st.text_input("", placeholder="Enter your url", label_visibility="collapsed")

llm = ChatGroq(model="llama3-8b-8192")

prompt_template = """
Provide the summary of the following content.
Content: {text}
"""

prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

if st.button("Summarize"):
    if not validators.url(url):
        st.error("Please enter a valid url")
    else:
        try:
            with st.spinner("Waiting...."):
                if "youtube.com" in url:
                    loader = YoutubeLoader.from_youtube_url(url, add_video_info=False, language=['hi', 'en', 'te'])
                else:
                    loader = UnstructuredURLLoader(urls=[url], ssl_verify=True, header={
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
                    })
                docs = loader.load()

                st.write(docs)
        except Exception as e:
            st.exception(f"Exception: {e}")