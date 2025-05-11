from sqlalchemy import Column, Integer, String, Numeric, Boolean, Text
from app.db.session import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    in_stock = Column(Boolean, default=True)