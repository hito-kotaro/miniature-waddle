from db.models import Team
from sqlalchemy.orm import Session
from schema import team_schema as t_sc


# アカウントのチームを名前で検索
def get_team_by_id(db: Session, account_id: int, team_name: str):
    team = (
        db.query(Team)
        .filter(Team.account_id == account_id, Team.name == team_name)
        .first()
    )
    return team


def create_team_query(db: Session, account_id: int, team_name: str, description: str):
    team = Team(name=team_name, description=description, account_id=account_id)
    print(team)
    db.add(team)
    db.commit()
    db.refresh(team)
    return team
