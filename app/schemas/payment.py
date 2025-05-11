from pydantic import BaseModel

class PaymentCreate(BaseModel):
    order_id: int
    amount: float
    currency: str = "usd"

class PaymentOut(PaymentCreate):
    id: int
    status: str
    stripe_payment_id: str
    class Config:
        orm_mode = True