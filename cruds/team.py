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

    team_list = []
    for t in teams:
        team = {
            "id": t.id,
            "name": t.name,
            "description": t.description,
            "penalty": 0,
            "point": 0,
            "created_at": t.created_at,
            "updated_at": t.updated_at,
        }
        team_list.append(team)

    print(team_list)
    return {"teams": team_list}
