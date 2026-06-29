import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
WEBSITE_URL = os.getenv("WEBSITE_URL")

# Models
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "openai/gpt-oss-120b"

# Chunking
CHUNK_SIZE = 700
CHUNK_OVERLAP = 100

# Retrieval
TOP_K = 4

# Memory
CHAT_HISTORY_LIMIT = 20