from sqlalchemy.orm import Session
from db.models import User
from utils.hash import Hash
import schema.user_schema as u_sc


def get_user_by_email_query(db: Session, email: str):
    """get user by email"""
    return db.query(User).filter(User.email == email).first()


def get_user_info_all(db: Session):
    """get user all"""

    # 全てのユーザー情報取得
    users = db.query(User).all()
    return {"users": users}


def create_user_query(db: Session, user: u_sc.UserRequest):
    """create user by email and password"""
    hashed_password = Hash.get_password_hash(user.password)

    user = User(
        email=user.email,
        name=user.name,
        hashed_password=hashed_password,
        role_id=user.role_id,
        guild_id=user.guild_id,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    print(user)
    return user
