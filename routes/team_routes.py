from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from cruds.team import get_team_by_id, create_team, get_all_team, get_user_by_id
import schema.team_schema as t_sc
from routes import router_base as rb
from cruds.auth import get_current_user

router = rb.create_router("team")


# チームを作成する


@router.post("/create")
def create_team_api(
    team: t_sc.CreateTeam,
    db: Session = Depends(rb.get_db),
    current_user: str = Depends(get_current_user),
):
    # アカウント内での重複確認
    team = get_team_by_id(
        db=db, account_id=current_user.account_id, team=create_team.name
    )
    if team:
        raise HTTPException(status_code=400, detail="team already exists")

    return create_team(
        db=db,
        account_id=current_user.account_id,
        team_name=create_team.name,
        description=create_team.description,
    )


# 全てのチームを取得
@router.get("/", response_model=t_sc.ResponseTeams)
def get_all_team_api(
    db: Session = Depends(rb.get_db),
    current_user: str = Depends(get_current_user),
):
    return get_all_team(db=db, account_id=current_user.account_id)


# 特定のIDのチームを取得
@router.get("/{id}", response_model=t_sc.ResponseTeam)
def get_team_api(
    id: int,
    db: Session = Depends(rb.get_db),
    current_user: str = Depends(get_current_user),
):
    return get_user_by_id(db=db, account_id=current_user.account_id, team_id=id)
