from pydantic import BaseModel
from typing import List


class PenaltyInfo(BaseModel):
    id: int
    title: str
    owner_id: int
    owner: str
    description: str
    penalty: int

    class Config:
        orm_mode = True


class PenaltyInfoAll(BaseModel):
    penalties: List[PenaltyInfo]

    class Config:
        orm_mode = True


class CreatePenalty(BaseModel):
    title: str
    description: str
    penalty: int


class IssuePenalty(BaseModel):
    penalty_id: int
    team_id: int
