from sqlalchemy.orm import Session
from db.models import Penalty, IssuedPenalty, Team
import schema.penalty_schema as p_sc
from cruds.user import get_user_name_by_id


def get_penalty(db: Session, account_id: int):
    penalties = db.query(Penalty).filter(Penalty.account_id == account_id).all()
    penalty_list = []

    for p in penalties:
        owner_name = get_user_name_by_id(
            db=db, account_id=account_id, user_id=p.owner_id
        )
        penalty: p_sc.PenaltyInfo = {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "owner_id": p.owner_id,
            "owner": owner_name,
            "penalty": p.penalty,
        }

        penalty_list.append(penalty)

    return {"penalties": penalty_list}


def create_penalty_query(
    db: Session, account_id: int, owner_id: int, new_penalty: p_sc.CreatePenalty
):
    penalty = Penalty(
        account_id=account_id,
        owner_id=owner_id,
        title=new_penalty.title,
        description=new_penalty.description,
        penalty=new_penalty.penalty,
    )

    db.add(penalty)
    db.commit()

    return {"message": penalty}


def issue_penalty_query(
    db: Session, account_id: int, authorizer_id: int, issue_data: p_sc.IssuePenalty
):
    issue = IssuedPenalty(
        penalty_id=issue_data.penalty_id,
        account_id=account_id,
        authorizer_id=authorizer_id,
        team_id=issue_data.team_id,
    )

    penalty = db.query(Penalty).filter(Penalty.id == issue_data.penalty_id).first()

    db.add(issue)
    add_penalty(db=db, team_id=issue_data.team_id, add_penalty=penalty.penalty)
    db.commit()
    return {"message": issue}


def add_penalty(db: Session, team_id: int, add_penalty: int):
    team = db.query(Team).filter(Team.id == team_id).first()
    team.penalty += add_penalty
    db.commit()
