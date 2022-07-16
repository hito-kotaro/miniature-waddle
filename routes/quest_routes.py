from fastapi import Depends
from sqlalchemy.orm import Session
from cruds.auth import get_current_user
import routes.router_base as rb
from cruds.quest import create_quest_query, get_quest_all
import schema.quest_schema as q_sc

router = rb.create_router("quest")


@router.get("/", response_model=q_sc.QuestInfoAll)
def get_quests(
    db: Session = Depends(rb.get_db), curent_user: str = Depends(get_current_user)
):
    return get_quest_all(db=db, account_id=curent_user.account_id)


@router.post("/create")
def create_quest(
    new_quest: q_sc.CreateQuest,
    db: Session = Depends(rb.get_db),
    curent_user: str = Depends(get_current_user),
):
    return create_quest_query(
        db=db,
        account_id=curent_user.account_id,
        owner_id=curent_user.id,
        new_quest=new_quest,
    )
