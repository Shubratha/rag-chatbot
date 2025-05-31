import os
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain.docstore.document import Document

def load_pdf(path):
    loader = PyPDFLoader(path)
    return loader.load()


def load_documents(folder_path: str):
    documents = []
    for file_name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file_name)

        if file_name.lower().endswith(".pdf"):
            loader = PyPDFLoader(full_path)
        elif file_name.lower().endswith(".docx"):
            loader = Docx2txtLoader(full_path)
        else:
            continue  # Skip unsupported file types

        docs = loader.load()
        documents.extend(docs)

    return documents


def convert_scraped_docs(scraped_docs):
    return [Document(page_content=doc["content"], metadata={"source": doc["url"]})
            for doc in scraped_docs]