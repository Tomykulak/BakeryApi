from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = "sqlite:///shop.db"

engine = create_engine(
    database_url,
    connect_args={"check_same_thread": False}
)
session_factory = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = session_factory()
    try:
        yield db
    finally:
        db.close()