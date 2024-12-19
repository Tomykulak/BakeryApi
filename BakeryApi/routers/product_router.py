from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.product_crud import create_product, get_product_by_id
from db.database import get_db
from schemas.product_schema import ProductResponse, ProductCreate

router: APIRouter = APIRouter(
    tags=["Product"],
    prefix="/product",
)


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product_by_id_endpoint(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/", response_model=ProductResponse)
async def create_product_endpoint(
    product_data: ProductCreate,
    db: Session = Depends(get_db),
):
    try:
        return create_product(db, product_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
