from config import WEBSITE_URL
from rag.loader import load_website 
from rag.splitter import split_documents
from rag.pinecone_db import upload_documents 

def run_ingestion():
    # Split comma-separated string into a clean Python list
    urls = [url.strip() for url in WEBSITE_URL.split(",")]
    all_chunks = []

    print(f"Starting ingestion for {len(urls)} URLs...")

    for url in urls:
        try:
            print(f"Scraping: {url}")
            # 1. Load the website data
            # NOTE: Your loader.py expects WEBSITE_URL from config natively, 
            # but if passing individual URLs, ensure loader.py accepts an argument.
            docs = load_website(url)
            print(f"Loaded {len(docs)} documents")
            
            # 2. Split it into smaller text chunks
            chunks = split_documents(docs)
            all_chunks.extend(chunks)

        except Exception as e:
            print(f"Error scraping {url}: {e}")
            continue

    # 3. Save all chunks to your Pinecone vector database
    if all_chunks:
        upload_documents(all_chunks)
        print("Successfully ingested all URLs to Pinecone!")
    else:
        print("No data was ingested.")

if __name__ == "__main__":
    run_ingestion()
