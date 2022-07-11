from fastapi import FastAPI
import db.models as models
from db.database import engine
from routes import auth_routes, user_routes, account_routes

# from db.migrate import reset_database


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# reset_database()

app.include_router(auth_routes.router)
app.include_router(user_routes.router)
app.include_router(account_routes.router)


@app.get("/")
def index():
    return {"message": "ok"}
