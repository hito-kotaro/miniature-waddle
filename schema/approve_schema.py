from datetime import datetime
from pydantic import BaseModel


class QuestInfo(BaseModel):
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
