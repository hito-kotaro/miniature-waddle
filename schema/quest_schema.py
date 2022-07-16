from pydantic import BaseModel
from typing import List


class QuestInfo(BaseModel):
    id: int
    title: str
    description: str
    reward: int
    owner: str
    status: bool

    class Config:
        orm_mode = True


class QuestInfoAll(BaseModel):
    quests: List[QuestInfo]


class CreateQuest(BaseModel):
    title: str
    description: str
    reward: int
