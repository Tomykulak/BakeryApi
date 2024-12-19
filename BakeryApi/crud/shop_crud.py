from typing import Optional

from sqlalchemy.orm import Session

from models.shop_model import Shop
from schemas.shop_schema import ShopCreate


def create_shop(
        db: Session,
        shop_data: ShopCreate
) -> Shop:
    try:
        new_shop = Shop(**shop_data.model_dump())
        db.add(new_shop)
        db.commit()
        db.refresh(new_shop)
        return new_shop
    except Exception as e:
        db.rollback()
        raise RuntimeError(f"Database error: {e}")

def get_shop_by_id(
        db: Session,
        shop_id: int
) -> Optional[Shop]:
    try:
        return db.query(Shop).filter(Shop.id == shop_id).first()
    except Exception as e:
        raise RuntimeError(f"Error retrieving shop by ID: {e}")
