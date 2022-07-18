from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class ApproveInfo(BaseModel):
    id: int
    title: str
    description: str
    applicant: str
    applicant_id: int
    quest_title: str
    quest_owner: str
    quest_description: str
    quest_created_at: datetime
    authorizer: Optional[str]
    reward: int
    status: str

    class Config:
        orm_mode = True


class ApproveInfoAll(BaseModel):
    approve_requests: List[ApproveInfo]


class CreateApproveRequest(BaseModel):
    title: str
    description: str
    quest_id: int


class UpdateApproveRequest(BaseModel):
    ar_id: int
    new_status: str
