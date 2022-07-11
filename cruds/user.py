from sqlalchemy.orm import Session
from db.models import User, Account
from utils.hash import Hash
import schema.user_schema as u_sc


def get_user_by_email_query(db: Session, email: str):
    """get user by email"""
    account = db.query(Account).filter(Account.email == email).first()
    user = db.query(User).filter(User.email == email).first()

    return (account is None) and (user is None)


def get_user_info_all(db: Session):
    """get user all"""

    # 全てのユーザー情報取得
    users = db.query(User).all()
    print(users)
    return {"users": users}


def create_user_query(db: Session, user: u_sc.UserCreate):
    """create user by email and password"""
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
