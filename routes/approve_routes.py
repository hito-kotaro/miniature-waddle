from fastapi import Depends
from sqlalchemy.orm import Session
from cruds.approve import (
    create_approve_request_query,
    get_approve_request_query,
    update_approve_request_query,
)
from routes import router_base as rb
from cruds.auth import get_current_user
import schema.approve_schema as a_sc

router = rb.create_router("approve")


@router.get("/", response_model=a_sc.ApproveInfoAll)
def get_approve_all_api(
    db: Session = Depends(rb.get_db), current_user: str = Depends(get_current_user)
):
    return get_approve_request_query(db=db, account_id=current_user.account_id)


@router.post("/create")
def create_approve_request_api(
    approve_requests: a_sc.CreateApproveRequest,
    db: Session = Depends(rb.get_db),
    current_user: str = Depends(get_current_user),
):
    return create_approve_request_query(
        db=db,
        account_id=current_user.account_id,
        user_id=current_user.id,
        ar=approve_requests,
    )


@router.put("/update")
def update_approve_request_api(
    update_request: a_sc.UpdateApproveRequest,
    db: Session = Depends(rb.get_db),
    current_user: str = Depends(get_current_user),
):
    return update_approve_request_query(
        db=db, authorizer_id=current_user.id, update_request=update_request
    )
