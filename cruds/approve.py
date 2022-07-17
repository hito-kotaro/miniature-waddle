from sqlalchemy.orm import Session
from cruds.user import get_user_name_by_id
from db.models import ApproveRequest, Quest
import schema.approve_schema as a_sc


def get_approve_request_query(db: Session, account_id: int):
    approves = (
        db.query(
            ApproveRequest,
            Quest,
        )
        .filter(
            ApproveRequest.quest_id == Quest.id,
        )
        .all()
    )

    approve_list = []
    for a in approves:
        print(a.ApproveRequest.authorizer_id)
        applicant = get_user_name_by_id(
            db=db, account_id=account_id, user_id=a.ApproveRequest.applicant_id
        )

        quest_owner = get_user_name_by_id(
            db=db, account_id=account_id, user_id=a.Quest.owner_id
        )

        approve = {
            "id": a.ApproveRequest.id,
            "title": a.ApproveRequest.title,
            "description": a.ApproveRequest.description,
            "applicant": applicant,
            "quest_title": a.Quest.title,
            "quest_owner": quest_owner,
            "quest_description": a.Quest.description,
            "quest_created_at": a.Quest.created_at,
            "reward": a.Quest.reward,
            "status": a.ApproveRequest.status,
        }

        if a.ApproveRequest.authorizer_id:
            authorizer = get_user_name_by_id(
                db=db, account_id=account_id, user_id=a.ApproveRequest.authorizer_id
            )
            print(authorizer)
            approve["authorizer"] = authorizer

        approve_list.append(approve)

    print(approve_list)
    return {"approve_requests": approve_list}


def create_approve_request_query(
    db: Session, account_id: int, user_id: int, ar: a_sc.CreateApproveRequest
):
    new_approve_request = ApproveRequest(
        account_id=account_id,
        title=ar.title,
        description=ar.description,
        quest_id=ar.quest_id,
        applicant_id=user_id,
        status="open",
    )

    db.add(new_approve_request)
    db.commit()

    return {"message": "ok"}


def update_approve_request_query(
    db: Session, authorizer_id: int, update_request: a_sc.UpdateApproveRequest
):
    ar = (
        db.query(ApproveRequest)
        .filter(ApproveRequest.id == update_request.ar_id)
        .first()
    )
    print(ar)
    ar.status = update_request.new_status
    ar.authorizer_id = authorizer_id
    db.commit()

    return {"message": f"update_id = {ar.id}"}
