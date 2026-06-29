from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: str
    question: str


class ChatResponse(BaseModel):
    answer: str


class ClearHistoryRequest(BaseModel):
    session_id: str


class HealthResponse(BaseModel):
    status: str