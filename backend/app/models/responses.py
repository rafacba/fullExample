from pydantic import BaseModel


class MessageResponse(BaseModel):
    """Response model for message endpoint"""
    message: str
    timestamp: str
    status: str


class HealthResponse(BaseModel):
    """Response model for health check endpoint"""
    status: str
    timestamp: str
