try:
    # Try the modern explicit path first
    from langchain.chains.retrieval import create_retrieval_chain
except ModuleNotFoundError:
    try:
        # Try the classic/legacy fallback path
        from langchain_classic.chains import create_retrieval_chain
    except ModuleNotFoundError:
        # Absolute fallback to legacy structures
        from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from rag.prompt import PROMPT
from rag.llm import get_llm
from rag.retriever import get_retriever

# Import the new function we made for temporary memory
from memory.history import get_chat_history

llm = get_llm()
retriever = get_retriever()

document_chain = create_stuff_documents_chain(
    llm,
    PROMPT
)

retrieval_chain = create_retrieval_chain(
    retriever,
    document_chain
)

def chatbot(session_id: str, question: str):
    # 1. Fetch the in-memory history container for this user session
    chat_history = get_chat_history(session_id)
    
    # 2. Get past messages formatted for the prompt
    # LangChain's internal memory keeps track of roles automatically
    history_messages = chat_history.messages
    
    # Format messages nicely into prose for your PROMPT's {history} variable
    formatted_history = ""
    for msg in history_messages:
        role = "Customer" if msg.type == "human" else "Zero Lifestyle AI Brand Expert"
        formatted_history += f"{role}: {msg.content}\n"

    # 3. Invoke the chain passing both the history and the new question
    result = retrieval_chain.invoke(
        {
            "input": question,
            "history": formatted_history
        }
    )
    
    answer = result["answer"]
    
    # 4. Save the new exchange into the in-memory store
    chat_history.add_user_message(question)
    chat_history.add_ai_message(answer)
    
    return {
        "answer": answer,
        "context": result["context"]
    }
