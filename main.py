from fastapi import FastAPI
import db.models as models
from db.database import engine

app = FastAPI()

models.User.metadata.create_all(bind=engine)


@app.get("/")
def index():
    return {"message": "ok"}
