import random
from sqlalchemy.orm import Session
from db.models import Account, Team, User
from utils.hash import Hash
from schema import account_schema as a_sc


def get_account_by_email_query(db: Session, email: str):
    """get user by email"""
    print(email)
    return db.query(Account).filter(Account.email == email).first()


def get_account_by_id_query(db: Session, id: id):
    """get user by email"""
    print(id)
    return db.query(Account).filter(Account.id == id).first()


def create_account_query(db: Session, account: a_sc.AccountCreate):
    """create user by email and password"""
    print(account)
    hashed_password = Hash.get_password_hash(account.password)
    root_role = 4

    while True:
        account_id = random.randrange(10**8, 10**9)
        if not get_account_by_id_query(db=db, id=account_id):
            break

    new_account = Account(
        id=account_id,
        email=account.email,
    )

    new_user = User(
        name=account.email,
        email=account.email,
        hashed_password=hashed_password,
        role_id=root_role,
        account_id=account_id,
        point=0,
    )

    db.add(new_user)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    print(new_account)
    return new_account


def get_score_info_query(db: Session, account_id: int, user_id: int, team_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    users = db.query(User).filter(User.account_id == account_id).all()
    team = db.query(Team).filter(Team.id == team_id).first()

    team_score = team.penalty
    account_score = 0

    for u in users:
        account_score += u.point
        if u.team_id == team_id:
            team_score += u.point

    print(user.point)
    print(team_score)
    print(account_score)
    # score = {"user_score": 10, "team_score": 20, "account_score": 30}
    return {"message": "ok"}
