from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def process_pdf(pdf_folder):
    """"
    Process PDFs in the folder
    """

    loader = PyPDFDirectoryLoader(pdf_folder)
    raw_docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
    )

    return text_splitter.split_documents(raw_docs)