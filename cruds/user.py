from sqlalchemy.orm import Session
from db.models import ApproveRequest, Quest, Role, Team, User, Account
from utils.hash import Hash
import schema.user_schema as u_sc


# チームIDからチームメンバーを検索する。
def get_users_by_team_id(db: Session, team_id):
    users = db.query(User).filter(User.team_id == team_id).all()
    return users


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
    account_id = current_user.account_id
    # アカウント内の全てのユーザー情報取得
    users = db.query(User).filter(User.account_id == account_id).all()
    print(users)
    return {"users": users}


def get_user_name_by_id(db: Session, account_id: int, user_id: int):
    user = (
        db.query(User).filter(User.account_id == account_id, User.id == user_id).first()
    )
    return user.name


def get_user_info_by_id(db: Session, current_user: dict):
    user = db.query(User).filter(User.id == current_user.id).first()
    print(user)
    return user


def create_user_query(db: Session, user: u_sc.UserCreate, account_id: int):
    """create user by email and password"""
    print(user)
    hashed_password = Hash.get_password_hash(user.password)

    user = User(
        email=user.email,
        name=user.name,
        hashed_password=hashed_password,
        account_id=account_id,
        role_id=user.role_id,
        team_id=user.team_id,
        point=0
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    print(user)
    return user


def summary_point_by_user_id(db: Session, user_id: int):
    approve_requests = (
        db.query(ApproveRequest, Quest)
        .filter(
            ApproveRequest.applicant_id == user_id,
            ApproveRequest.status == "approved",
            ApproveRequest.quest_id == Quest.id,
        )
        .all()
    )

    for a in approve_requests:
        print(a.ApproveRequest.id)
        print(a.Quest.reward)
    point = 0
    return point


def get_user_small_info_by_id(db: Session, user_id: int):
    user = (
        db.query(User, Role).filter(User.id == user_id, User.role_id == Role.id).first()
    )

    team_name = ""
    point = summary_point_by_user_id(db=db, user_id=user_id)

    if user.User.team_id:
        team = db.query(Team).filter(Team.id == user.User.team_id).first()
        team_name = team.name
    else:
        team_name = "no team"

    small_info: u_sc.SmallUserInfo = {
        "name": user.User.name,
        "team": team_name,
        "role": user.Role.name,
        "point": point,
    }

    return small_info
