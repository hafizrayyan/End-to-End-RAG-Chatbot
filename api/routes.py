from fastapi import APIRouter, HTTPException

from api.schemas import (
    ChatRequest,
    ChatResponse,
    ClearHistoryRequest,
    HealthResponse
)

from rag.chain import chatbot

from memory.history import clear_history

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse
)
async def health():

    return {
        "status": "healthy"
    }


@router.post(
    "/chat",
    response_model=ChatResponse
)
async def chat(data: ChatRequest):

    try:

        response = chatbot(
            session_id=data.session_id,
            question=data.question
        )

        return {
            "answer": response["answer"]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/clear-history")
async def delete_history(
    data: ClearHistoryRequest
):

    try:

        clear_history(
            data.session_id
        )

        return {
            "message": "Conversation deleted successfully."
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )