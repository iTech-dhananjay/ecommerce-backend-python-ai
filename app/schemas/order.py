from pydantic import BaseModel

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    total_price: float

class OrderOut(OrderCreate):
    id: int
    status: str
    class Config:
        orm_mode = True