import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    PPLX_API_KEY = os.getenv('PPLX_API_KEY')
    PPLX_URL = os.getenv("PERPLEXITY_URL")
    PPLX_MODEL = os.getenv('PPLX_MODEL') or "llama-3.1-sonar-small-128k-online"

    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')