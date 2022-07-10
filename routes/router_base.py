from fastapi import APIRouter
from db.database import SessionLocal


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
    return db


def create_router(prefix: str):
    return APIRouter(prefix=f"/{prefix}", tags=[prefix])
