import os
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings

EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL")

class VectorDB:
    def __init__(self, documents=None, load_path=None):
        # self.embeddings = OpenAIEmbeddings()
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") # EMBEDDING_MODEL_NAME)

        if load_path:
            self.db = FAISS.load_local(load_path, self.embeddings, allow_dangerous_deserialization=True)
        elif documents:
            self.db = FAISS.from_documents(documents, self.embeddings)
        else:
            raise ValueError("Either documents or load_path must be provided.")

    def similarity_search(self, query, k=3):
        return self.db.similarity_search_with_score(query, k=k)

    def retriever(self, k=3):
        return self.db.as_retriever(search_kwargs={"k": k})

    def save(self, path: str):
        self.db.save_local(path)
