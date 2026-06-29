from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import InMemoryChatMessageHistory

# This global dictionary holds active chat sessions in your server's RAM
_memory_store = {}

def get_chat_history(session_id: str) -> BaseChatMessageHistory:
    """
    Retrieves or creates a temporary in-memory chat history for a session.
    """
    if session_id not in _memory_store:
        _memory_store[session_id] = InMemoryChatMessageHistory()
    return _memory_store[session_id]

def clear_history(session_id: str):
    """
    Deletes the session history from the store.
    """
    if session_id in _memory_store:
        del _memory_store[session_id]