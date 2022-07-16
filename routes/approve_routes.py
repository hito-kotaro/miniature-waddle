from fastapi import Depends
from sqlalchemy.orm import Session
from routes import router_base as rb
from cruds.auth import get_current_user


router = rb.create_router("approve")


@router.get("/")
def get_approve_all_api(
    db: Session = Depends(rb.get_db), current_user: str = Depends(get_current_user)
):
    return {"message": "ok"}
