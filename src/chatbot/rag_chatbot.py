from src.data_ingestion.pdf_processor import load_documents
from src.vector_store.vector_db import VectorDB
from src.generation.llm_handler import RAGGenerator
from src.retrieval.retriever import Retriever
from langchain.embeddings import HuggingFaceEmbeddings

class ChatBot:
    # def __init__(self, pdf_path):
    #     docs = load_documents(pdf_path)
    #     vector_db = VectorDB(docs)
    #     self.generator = RAGGenerator(vector_db.retriever())
    #
    # def chat(self, query):
    #     return self.generator.answer_query(query)

    def __init__(self):
        embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vector_store_path = "data/vector_store/faiss_index"
        vector_db = VectorDB(load_path=vector_store_path)
        # self.retriever = Retriever(vector_store_path, embedding_model)
        self.retriever = vector_db.retriever()
        self.generator = RAGGenerator()

    def chat(self, query):
        # context_docs = self.retriever.retrieve(query)
        context_docs = self.retriever.get_relevant_documents(query)
        context_text = "\n".join(doc.page_content for doc in context_docs)

        return self.generator.answer_query(query, context_text)