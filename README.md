# rag-chatbot
A Retrieval-Augmented Generation (RAG) chatbot built to assist users with support-related queries based on official documentation from:
- 📄 Documentation PDFs
- https://www.angelone.in/support

It answers only from these sources and responds with "I don't know" for anything beyond them.

⸻

### 🚀 Features 
- 🔍 Retrieval from PDFs and support site 
- LLM-based response generation 
- FAISS + Sentence Transformers for vector store 
- Local or OpenAI LLM support 
- Clean, modular architecture 
- Streamlit frontend

⸻

### 🛠️ Tech Stack 
- Backend: Python, LangChain, FAISS, SentenceTransformers 
- Frontend: Streamlit 
- Embedding Models: sentence-transformers/all-MiniLM-L6-v2
- LLMs: OpenAI / Falcon / Any compatible local model
- Data Sources: PDFs, Web scraping via BeautifulSoup

⸻


### 🧪 Setup Instructions

1. <b>Clone the repo</b>
   ```commandline
    git clone https://github.com/yourusername/rag-chatbot.git
    cd rag-chatbot
   ```
2. <b>Install dependencies</b>
   ```commandline
    pip install -r requirements.txt
   ```
3. <b>Configure environment</b>
    <br>Copy .env.example and update with your API keys and model configs.
   ```
    cp .env.example .env
   ```
4. <b>Ingest your data</b>
    <br>Ensure your PDFs are in data/raw/pdfs/, and then run:
   ```commandline
    python scripts/create_vector_store.py
   ```
   <br>This will:
   - Load PDF/web data
   - Generate embeddings
   - Save to FAISS vector DB

⸻

### ▶️ Run the App
```commandline
streamlit run app/main.py
```
- Visit: http://localhost:8501
- Ask questions like “How to reset my password?”
- If the answer is out-of-scope, you’ll see: "I don't know"

⸻

### 📬 Contact

For issues or contributions, open an issue or [email](mailto:shubratha.leo@gmail.com).