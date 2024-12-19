from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud.shop_crud import create_shop, get_shop_by_id, get_all_shops
from db.database import get_db
from schemas.shop_schema import ShopCreate, ShopResponse
from fastapi.exceptions import HTTPException

router: APIRouter = APIRouter(
    tags=["Shop"],
    prefix="/shop",
)

@router.get("/", response_model=list[ShopResponse])
async def get_all_shops_endpoint(db: Session = Depends(get_db)):
    try:
        return get_all_shops(db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.get("/{shop_id}", response_model=ShopResponse)
async def get_shop_endpoint(shop_id: int, db: Session = Depends(get_db)):
    shop = get_shop_by_id(db, shop_id)
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")
    return shop

@router.post("/", response_model=ShopResponse)
async def create_shop_endpoint(
    shop_data: ShopCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_shop(db, shop_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

