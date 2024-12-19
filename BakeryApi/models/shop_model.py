from sqlalchemy import Column, Integer, String, DateTime

from db.database import Base


# Define the Shop model
class Shop(Base):
    __tablename__ = "shop"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    open_time = Column(DateTime, nullable=False)
