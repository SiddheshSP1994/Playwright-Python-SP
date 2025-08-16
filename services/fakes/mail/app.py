"""A simple email sender fake using FastAPI.

This service accepts a request to send an email and always returns success.  It
can be extended to store sent messages for later inspection.
"""
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI(title="Fake Mail Service")


class EmailRequest(BaseModel):
    to: EmailStr = Field(..., description="Recipient email address")
    subject: str = Field(..., description="Email subject")
    body: str = Field(..., description="Email body")


class EmailResponse(BaseModel):
    status: str
    message_id: str


@app.post("/send", response_model=EmailResponse)
def send_email(req: EmailRequest) -> EmailResponse:
    """Simulate sending an email and return a dummy message ID."""
    message_id = f"MSG{abs(hash(req.to + req.subject)) % 1000000:06d}"
    return EmailResponse(status="sent", message_id=message_id)