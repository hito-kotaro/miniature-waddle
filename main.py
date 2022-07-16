from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import db.models as models
from db.database import engine
from routes import auth_routes, user_routes, account_routes, team_routes, quest_routes

# from db.migrate import reset_database


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# reset_database()

app.include_router(auth_routes.router)
app.include_router(user_routes.router)
app.include_router(account_routes.router)
app.include_router(team_routes.router)
app.include_router(quest_routes.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"message": "ok"}
