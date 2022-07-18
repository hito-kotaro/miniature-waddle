from fastapi import Depends
from sqlalchemy.orm import Session
from cruds.auth import get_current_user
from cruds.penalty import create_penalty_query, get_penalty, issue_penalty_query
import routes.router_base as rb
import schema.penalty_schema as p_sc


router = rb.create_router("penalty")


@router.get("/", response_model=p_sc.PenaltyInfoAll)
def get_penalty_api(
    db: Session = Depends(rb.get_db),
    current_user: str = Depends(get_current_user),
):
    return get_penalty(db=db, account_id=current_user.account_id)


@router.post("/create")
def create_penalty(
    new_penalty: p_sc.CreatePenalty,
    db: Session = Depends(rb.get_db),
    current_user: str = Depends(get_current_user),
):
    return create_penalty_query(
        db=db,
        account_id=current_user.account_id,
        owner_id=current_user.id,
        new_penalty=new_penalty,
    )


@router.post("/issue")
def issue_penalty(
    issue_data: p_sc.IssuePenalty,
    db: Session = Depends(rb.get_db),
    current_user: str = Depends(get_current_user),
):
    return issue_penalty_query(
        db=db,
        account_id=current_user.account_id,
        authorizer_id=current_user.id,
        issue_data=issue_data,
    )
