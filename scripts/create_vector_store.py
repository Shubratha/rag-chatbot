from src.data_ingestion.pdf_processor import load_documents, convert_scraped_docs
from src.data_ingestion.web_scraper import scrape_website
from src.vector_store.vector_db import VectorDB
from config.settings import settings

if __name__ == "__main__":
    # Load local files (PDFs & DOCX)
    doc_files = load_documents(settings.PDF_DIR)

    # Scrape the AngelOne support site
    scraped_pages = scrape_website(settings.ANGELONE_BASE_URL)
    web_docs = convert_scraped_docs(scraped_pages)

    # Combine all docs
    all_docs = doc_files + web_docs

    # Create vector store
    vector_db = VectorDB(documents=all_docs)
    vector_db.save("data/vector_store/faiss_index")
    print(f"✅ Indexed {len(all_docs)} documents from PDFs and website.")
