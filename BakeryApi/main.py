from fastapi import FastAPI

from db.database import engine, Base as database
from routers.shop_router import router as shop_router
from routers.product_router import router as product_router
database.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(shop_router)
app.include_router(product_router)

@app.get("/")
async def root():
    return {"Root"}