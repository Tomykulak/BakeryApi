from typing import Optional, Type

from sqlalchemy.orm import Session

from models.product_model import Product
from schemas.product_schema import ProductCreate


def create_product(
        db: Session,
        product_data: ProductCreate
) -> Product:
    try:
        new_product = Product(
            name=product_data.name,
            count=product_data.count,
            baked_date=product_data.baked_date,
            shelf_life=product_data.shelf_life
        )
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    except Exception as e:
        db.rollback()
        raise RuntimeError(f"Database error: {e}")

def get_product_by_id(
        db: Session,
        product_id: int
) -> Optional[Type[Product]]:
    try:
        return db.query(Product).filter(Product.id == product_id).first()
    except Exception as e:
        raise RuntimeError(f"Database error: {e}")