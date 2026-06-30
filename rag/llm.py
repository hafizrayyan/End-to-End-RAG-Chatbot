from langchain_google_genai import ChatGoogleGenerativeAI

from config import (
    GROQ_API_KEY,
    LLM_MODEL
)


def get_llm():

    llm = ChatGoogleGenerativeAI(
        api_key=GROQ_API_KEY,
        model=LLM_MODEL,
       )

    return llm
