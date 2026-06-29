from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore

from config import (
    PINECONE_API_KEY,
    PINECONE_INDEX
)

from rag.embeddings import get_embeddings

pc = Pinecone(
    api_key=PINECONE_API_KEY
)


def get_vector_store():

    embeddings = get_embeddings()

    index = pc.Index(
        PINECONE_INDEX
    )

    vector_store = PineconeVectorStore(
        index=index,
        embedding=embeddings
    )

    return vector_store


def upload_documents(chunks):

    vector_store = get_vector_store()

    vector_store.add_documents(
        documents=chunks
    )

    print("Documents uploaded successfully.")