from db.models import Team
from sqlalchemy.orm import Session


# アカウントのチームを名前で検索
def get_team_by_id(db: Session, account_id: int, team_name: str):
    team = (
        db.query(Team)
        .filter(Team.account_id == account_id, Team.name == team_name)
        .first()
    )
    return team


def create_team(db: Session, account_id: int, team_name: str, description: str):
    team = Team(name=team_name, description=description, account_id=account_id)
    db.add(team)
    db.commit()
    db.refresh(team)
    return team


def get_all_team(db: Session, account_id: int):
    teams = db.query(Team).filter(Team.account_id == account_id).all()
    return {"teams": teams}


def get_user_by_id(db: Session, account_id: int, team_id: int):
    team = (
        db.query(Team).filter(Team.account_id == account_id, Team.id == team_id).first()
    )

    return team
