from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.sql import func
from app.db.session import Base

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    amount = Column(Numeric(10, 2), nullable=False)
    currency = Column(String(10), default="usd")
    stripe_payment_id = Column(String(100))
    status = Column(String(50), default="initiated")
    created_at = Column(DateTime(timezone=True), server_default=func.now())