import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    PDF_DIR: str = "data/raw/pdfs"
    ANGELONE_BASE_URL: str = "https://www.angelone.in/support"

settings = Settings()
