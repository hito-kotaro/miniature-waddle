from http.client import HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from cruds.account import get_account_by_email_query, create_account_query
from schema import account_schema as a_sc
import routes.router_base as rb

# from schema import auth_schema as auth_sc
# from passlib.context import CryptContext


router = rb.create_router("account")


@router.post("/create")
def create_access_token(account: a_sc.AccountCreate, db: Session = Depends(rb.get_db)):
    db_account = get_account_by_email_query(db=db, email=account.email)
    if db_account:
        raise HTTPException(status_code=400, detail="account already registerd")
    return create_account_query(db=db, account=account)
