from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timedelta
from db.database import Base


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    count = Column(Integer, nullable=False)
    baked_date = Column(DateTime, nullable=False)
    shelf_life = Column(Integer, nullable=False)  # Shelf life in days

    @hybrid_property
    def expiration_date(self) -> datetime:
        return self.baked_date + timedelta(days=self.shelf_life)
