from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional


class ProductBase(BaseModel):
    name: str
    count: int
    baked_date: datetime

    class Config:
        orm_mode = True  # Allows compatibility with ORM models


class ProductCreate(ProductBase):
    shelf_life: int  # Shelf life in days (e.g., 2 days)

    def calculate_expiration_date(self) -> datetime:
        return self.baked_date + timedelta(days=self.shelf_life)


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    count: Optional[int] = None
    baked_date: Optional[datetime] = None

    class Config:
        orm_mode = True


class ProductResponse(ProductBase):
    expiration_date: datetime  # Dynamically calculated

    class Config:
        orm_mode = True
