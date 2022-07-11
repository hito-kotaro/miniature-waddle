from sqlalchemy.orm import Session
from db.models import Account
from utils.hash import Hash
from schema import account_schema as a_sc


def get_account_by_email_query(db: Session, email: str):
    """get user by email"""
    print(email)
    return db.query(Account).filter(Account.email == email).first()


def create_account_query(db: Session, account: a_sc.AccountCreate):
    """create user by email and password"""
    hashed_password = Hash.get_password_hash(account.password)

    new_account = Account(
        email=account.email,
        hashed_password=hashed_password,
    )

    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    print(new_account)
    return new_account
