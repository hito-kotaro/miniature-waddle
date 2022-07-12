from sqlalchemy.orm import Session
from db.models import User, Account
from utils.hash import Hash
import schema.user_schema as u_sc


def get_user_by_email_query(db: Session, email: str):
    """get user by email"""
    account = db.query(Account).filter(Account.email == email).first()
    user = (
        db.query(User)
        .filter(
            User.email == email,
        )
        .first()
    )

    return (account is None) and (user is None)


def get_user_all_in_account(db: Session, current_user):
    """get user all"""
    account_id = current_user["account_id"]
    # アカウント内の全てのユーザー情報取得
    users = db.query(User).filter(User.account_id == account_id).all()
    print(users)
    return {"users": users}


def get_user_info_by_id(db: Session, current_user: dict):
    user = db.query(User).filter(User.id == current_user.id).first()
    print(user)
    return {"message": "ok"}


def create_user_query(db: Session, user: u_sc.UserCreate):
    """create user by email and password"""
    print(user)
    hashed_password = Hash.get_password_hash(user.password)

    if user.role_id is None:
        role_id = None
    else:
        role_id = user.role_id

    if user.team_id is None:
        team_id = None
    else:
        team_id = user.team_id

    user = User(
        email=user.email,
        name=user.name,
        hashed_password=hashed_password,
        account_id=user.account_id,
        role_id=role_id,
        team_id=team_id,
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    print(user)
    return user
