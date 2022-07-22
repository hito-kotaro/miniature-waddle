from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from cruds.account import (
    get_account_by_email_query,
    create_account_query,
    get_score_info_query,
)
from schema import account_schema as a_sc
import routes.router_base as rb
from cruds.auth import get_current_user

# from schema import auth_schema as auth_sc
# from passlib.context import CryptContext


router = rb.create_router("account")


@router.post("/create")
def create_account(account: a_sc.AccountCreate, db: Session = Depends(rb.get_db)):
    db_account = get_account_by_email_query(db=db, email=account.email)
    if db_account:
        raise HTTPException(status_code=400, detail="account already registerd")
    return create_account_query(db=db, account=account)


@router.get("/score")
def get_score_info_api(
    db: Session = Depends(rb.get_db), current_user: str = Depends(get_current_user)
):
    return get_score_info_query(
        db=db,
        account_id=current_user.account_id,
        user_id=current_user.id,
        team_id=current_user.team_id,
    )
