# from fastapi import Depends
# from sqlalchemy.orm import Session
# from cruds.auth import get_current_user
from cruds.penalty import get_penalty
import routes.router_base as rb


router = rb.create_router("penalty")


@router.get("/")
def get_penalty_api():
    return get_penalty()
