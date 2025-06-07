import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    OPENAI_API_BASE = "https://openrouter.ai/api/v1"
    MODEL ="mistralai/mistral-7b-instruct"
    # MODEL = "openai/gpt-4o"
    
