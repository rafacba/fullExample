from fastapi import APIRouter
from datetime import datetime
from app.models.responses import MessageResponse, HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    }


@router.get("/message", response_model=MessageResponse)
async def get_message():
    """Get message endpoint that returns a greeting from the backend"""
    return {
        "message": "Hello from FastAPI! This message is coming from the backend.",
        "timestamp": datetime.now().isoformat(),
        "status": "success"
    }
