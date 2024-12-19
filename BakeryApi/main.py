from fastapi import FastAPI

from db.database import engine, Base as database
from routers.shop_router import router as shop_router

database.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(shop_router)

@app.get("/")
async def root():
    return {"Root"}