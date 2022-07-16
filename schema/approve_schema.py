from datetime import datetime
from typing import List
from pydantic import BaseModel


class ApproveInfo(BaseModel):
    id: int
    title: str
    description: str
    applicant: str
    quest_title: str
    quest_owner: str
    quest_description: str
    quest_created_at: datetime
    reward: int
    status: str

    class Config:
        orm_mode = True


class ApproveInfoAll(BaseModel):
    approve_requests: List[ApproveInfo]


class CreateApproveRequest(BaseModel):
    account_id: int
    title: str
    description: str
    quest_id: int
    applicant_id: int
    status: str
