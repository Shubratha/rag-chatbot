# from langchain.chat_models import ChatOpenAI
# from langchain.chains import RetrievalQA
from transformers import pipeline


class RAGGenerator:
    # def __init__(self, retriever):
    #     self.qa = RetrievalQA.from_chain_type(
    #         llm=ChatOpenAI(temperature=0),
    #         retriever=retriever,
    #         return_source_documents=True
    #     )

    # def answer_query(self, query):
    #     result = self.qa({"query": query})
    #     if not result['source_documents']:
    #         return "I don't know"
    #     return result['result']

    def __init__(self):
        self.generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",  # lightweight and free to use
            max_new_tokens=512
        )

    def answer_query(self, query: str, context: str = "") -> str:
        prompt = (
            "You are a helpful assistant. Answer the question using only the given context. "
            "If the answer is not in the context, respond with 'I don't know.'\n\n"
            f"Context:\n{context}\n\nQuestion: {query}"
        )
        response = self.generator(prompt)[0]["generated_text"]
        return response.strip()


