from sqlalchemy.orm import Session
from db.models import Quest, User
import schema.quest_schema as q_sc


# アカウント内の全てのクエストを取得する
def get_quest_all(db: Session, account_id: int):

    quests = db.query(Quest, User).filter(Quest.owner_id == User.id).all()
    quest_list = []

    for q in quests:
        quest = {
            "id": q.Quest.id,
            "title": q.Quest.title,
            "description": q.Quest.description,
            "reward": q.Quest.reward,
            "owner": q.User.name,
            "status": q.Quest.status,
        }

        quest_list.append(quest)
    print("test")
    print(quest_list)

    return {"quests": quest_list}


def create_quest_query(
    db: Session, account_id: int, owner_id: int, new_quest: q_sc.CreateQuest
):

    quest = Quest(
        account_id=account_id,
        title=new_quest.title,
        description=new_quest.description,
        reward=new_quest.reward,
        owner_id=owner_id,
        status=True,
    )

    db.add(quest)
    db.commit()
    return {"message": "ok"}
