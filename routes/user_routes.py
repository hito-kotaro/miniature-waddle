from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
import schema.user_schema as u_sc
from routes import router_base as rb
from cruds.user import (
    create_user_query,
    get_user_by_email_query,
    get_user_info_all,
)
from cruds.auth import get_current_user

router = rb.create_router("user")


@router.post("/create")
def create_user_api(create_user: u_sc.UserCreate, db: Session = Depends(rb.get_db)):
    db_user = get_user_by_email_query(db=db, email=create_user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="email already registered")
    return create_user_query(db=db, user=create_user)


# 全てのユーザーの情報取得
@router.get("/", response_model=u_sc.UserInfoAll)
def get_user_all_api(
    db: Session = Depends(rb.get_db),
    current_user: str = Depends(get_current_user),
):
    return get_user_info_all(db=db)
