from fastapi import FastAPI
import db.models as models
from db.database import engine
from routes import auth_routes


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)


@app.get("/")
def index():
    return {"message": "ok"}
