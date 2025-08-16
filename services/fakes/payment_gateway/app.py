"""A simple payment gateway fake using FastAPI.

This service accepts a payment request and returns a dummy transaction ID.
In a real project you would implement proper integration with a payment
processor or use a mocking framework.
"""
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Fake Payment Gateway")


class PaymentRequest(BaseModel):
    amount: float = Field(..., gt=0, description="Payment amount")
    currency: str = Field("INR", description="Currency code")


class PaymentResponse(BaseModel):
    status: str
    transaction_id: str


@app.post("/pay", response_model=PaymentResponse)
def pay(req: PaymentRequest) -> PaymentResponse:
    """Simulate a payment and return a fake transaction ID."""
    tx_id = f"TX{int(req.amount * 1000):06d}"
    return PaymentResponse(status="success", transaction_id=tx_id)