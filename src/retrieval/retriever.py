from typing import List
from langchain.vectorstores import FAISS
from langchain.embeddings.base import Embeddings
from langchain.docstore.document import Document
import os

class Retriever:
    def __init__(self, vector_store_path: str, embedding_model: Embeddings, k: int = 4):
        self.vector_store_path = vector_store_path
        self.embedding_model = embedding_model
        self.k = k  # number of docs to retrieve

        if not os.path.exists(vector_store_path):
            raise ValueError(f"Vector store path does not exist: {vector_store_path}")

        self.db = FAISS.load_local(vector_store_path, self.embedding_model, allow_dangerous_deserialization=True)

    def retrieve(self, query: str) -> List[Document]:
        """
        Given a user query, returns top-k most relevant documents.
        """
        results = self.db.similarity_search(query, k=self.k)
        return results