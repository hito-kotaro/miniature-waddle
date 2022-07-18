from pydantic import BaseModel
from typing import List, Optional


class UserInfo(BaseModel):
    id: int
    name: str
    email: str
    point: int
    role_id: Optional[int]
    team_id: Optional[int]

    class Config:
        orm_mode = True


class SmallUserInfo(BaseModel):
    name: str
    team: str
    role: str
    point: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role_id: int
    team_id: Optional[int]


class UserInfoAll(BaseModel):
    """get user info all"""

    users: List[UserInfo]

    class Config:
        orm_mode = True
