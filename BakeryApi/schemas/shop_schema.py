from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ShopBase(BaseModel):
    name: str
    address: str
    open_time: datetime

    class Config:
        orm_mode = True  # Allows compatibility with ORM models


class ShopCreate(ShopBase):
    pass


class ShopUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    open_time: Optional[datetime] = None

    class Config:
        orm_mode = True  # Consistency for ORM compatibility


class ShopResponse(ShopBase):
    id: int

    class Config:
        orm_mode = True
