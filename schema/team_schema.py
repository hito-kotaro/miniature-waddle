from typing import List, Optional
from pydantic import BaseModel


class CreateTeam(BaseModel):
    name: str
    description: Optional[str]


class ResponseTeam(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True


class ResponseTeams(BaseModel):
    teams: List[ResponseTeam]

    class Config:
        orm_mode = True
