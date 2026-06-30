import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
WEBSITE_URL ={
    "https://zerolifestyle.co/pages/smart-watches",
    "https://zerolifestyle.co/products/luna-smart-watch",
    "https://zerolifestyle.co/products/edge-smartwatch",
    "https://zerolifestyle.co/products/bolt-pro",
    "https://zerolifestyle.co/products/crown-smartwatch",
    "https://zerolifestyle.co/products/icon-smartwatch",
    "https://zerolifestyle.co/products/terra-fit-smart-watch",
    "https://zerolifestyle.co/products/lunar-360-smartwatch",
    "https://zerolifestyle.co/products/navigator-smartwatch",
    "https://zerolifestyle.co/products/elite-smart-watch",
    "https://zerolifestyle.co/products/vision-smartwatch",
    "https://zerolifestyle.co/products/visionary-smartwatch",
    "https://zerolifestyle.co/products/legacy-smartwatch",
    "https://zerolifestyle.co/products/armour-smart-watch",
    "https://zerolifestyle.co/products/regal-smartwatch",
    "https://zerolifestyle.co/products/ignite-smart-watch",
    "https://zerolifestyle.co/products/qube-smartwatch",
    "https://zerolifestyle.co/products/jewel-smartwatch",
    "https://zerolifestyle.co/products/orbit-2",
    "https://zerolifestyle.co/products/jaguar",
    "https://zerolifestyle.co/products/revolt-smart-watch",
    "https://zerolifestyle.co/products/vogue-smartwatch",
    "https://zerolifestyle.co/products/royale-smartwatch",
    "https://zerolifestyle.co/products/luna-pro",
    "https://zerolifestyle.co/products/revoltt-pro-smartwatch",
    "https://zerolifestyle.co/products/meta-smart-watch",
    "https://zerolifestyle.co/products/meta-smart-watch",
    "https://zerolifestyle.co/products/glory-smartwatch",
    "https://zerolifestyle.co/products/phantom-pro-smart-watch",
    "https://zerolifestyle.co/pages/terms-and-conditions",
    "https://zerolifestyle.co/pages/shipping-policy",
    "https://zerolifestyle.co/pages/privacy-policy",
    "https://zerolifestyle.co/pages/warranty-policy",
    "https://zerolifestyle.co/pages/corporate-policy"
    
}

# Models
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = os.getenv("LLM_MODEL")


# Chunking
CHUNK_SIZE = 700
CHUNK_OVERLAP = 200

# Retrieval
TOP_K = 3

# Memory
CHAT_HISTORY_LIMIT = 5
