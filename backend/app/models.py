from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class ProductBase(SQLModel):
    name: str
    sku: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = 0.0
    stock: Optional[int] = 0

class Product(ProductBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)