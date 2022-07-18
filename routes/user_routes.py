from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
import schema.user_schema as u_sc
from routes import router_base as rb
from cruds.user import (
    create_user_query,
    get_user_by_email_query,
    get_user_all_in_account,
    get_user_small_info_by_id,
    updpate_user_password,
)
from cruds.auth import get_current_user

router = rb.create_router("user")


@router.post("/create")
def create_user_api(
    create_user: u_sc.UserCreate,
    db: Session = Depends(rb.get_db),
    current_user: str = Depends(get_current_user),
):
    print(create_user)
    # if db_userでraiseできるようにgeet_user_by_email_queryを修正する
    db_user = get_user_by_email_query(db=db, email=create_user.email)
    if not db_user:
        raise HTTPException(status_code=400, detail="email already registered")
    return create_user_query(
        db=db, user=create_user, account_id=current_user.account_id
    )


# アカウント内の全てのユーザーの情報取得
@router.get("/", response_model=u_sc.UserInfoAll)
def get_user_all_api(
    db: Session = Depends(rb.get_db),
    current_user: str = Depends(get_current_user),
):
    return get_user_all_in_account(db=db, current_user=current_user)


# 特定IDのユーザー情報を取得
@router.get("/{id}", response_model=u_sc.SmallUserInfo)
def get_user_api(
    id: int,
    db: Session = Depends(rb.get_db),
    current_user: str = Depends(get_current_user),
):
    return get_user_small_info_by_id(db=db, user_id=current_user.id)


# パスワードの変更
@router.patch("/password")
def upodate_password_api(
    update: u_sc.UserPassUpdate,
    db: Session = Depends(rb.get_db),
    current_user: str = Depends(get_current_user),
):
    return updpate_user_password(
        db=db, user_id=current_user.id, new_password=update.new_password
    )
