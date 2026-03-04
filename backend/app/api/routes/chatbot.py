"""
Chatbot API Router
Provides endpoints for chatbot functionality
"""

from typing import List, Optional

# Import the validated constants from your new config
from core.config import GEMINI_API_KEY, PUSHOVER_TOKEN, PUSHOVER_USER
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from services.chatbot_service import ChatbotService

router = APIRouter(prefix="/api/v1/chatbot", tags=["chatbot"])


# Initialize chatbot service
def get_chatbot_service() -> ChatbotService:
    """Dependency to get chatbot service instance using validated config"""
    # We use the imported constants which are guaranteed strings by config.py
    return ChatbotService(
        gemini_api_key=GEMINI_API_KEY,
        pushover_user=PUSHOVER_USER,
        pushover_token=PUSHOVER_TOKEN,
    )


# Request/Response models
class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: str


class ChatRequest(BaseModel):
    message: str
    # Fixed the type hint error by removing Optional and defaulting to []
    history: List[Message] = []


class ChatResponse(BaseModel):
    response: str
    model: str = "gemini-2.5-flash"


class ContactRequest(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    message: Optional[str] = None


# Endpoints
@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest, chatbot: ChatbotService = Depends(get_chatbot_service)
):
    """
    Chat with the AI assistant
    """
    try:
        # Pydantic v2 uses .model_dump() instead of .dict()
        history_dicts = [msg.model_dump() for msg in request.history]

        response = chatbot.chat(message=request.message, history=history_dicts)

        return ChatResponse(response=response)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat error: {str(e)}")


@router.post("/contact")
async def record_contact(
    request: ContactRequest, chatbot: ChatbotService = Depends(get_chatbot_service)
):
    """
    Record contact information directly
    """
    try:
        # Removed unused variable 'result' to satisfy Ruff linting
        chatbot._record_user_details(
            email=request.email,
            name=request.name or "Not provided",
            notes=request.message or "Direct contact form submission",
        )

        return {"success": True, "message": "Contact information recorded successfully"}

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to record contact: {str(e)}"
        )


@router.get("/health")
async def chatbot_health():
    """Check if chatbot service is available using the central config"""
    if not GEMINI_API_KEY:
        return {"status": "unhealthy", "message": "GEMINI_API_KEY not configured"}

    return {
        "status": "healthy",
        "model": "gemini-2.0-flash-exp",
        "features": ["chat", "contact_recording", "push_notifications"],
    }
