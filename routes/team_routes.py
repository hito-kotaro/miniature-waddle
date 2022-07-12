from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
import schema.team_schema as t_sc
from routes import router_base as rb
from cruds.auth import get_current_user

router = rb.create_router("team")


# チームを作成する


# @router.post("/create")
# def create_user_api(
#     create_team: t_sc.CreateTeam,
#     db: Session = Depends(rb.get_db),
#     current_user: str = Depends(get_current_user),
# ):
#     return {"message": "create_team"}


# 全てのチームを取得


# 特定のIDのチームを取得
