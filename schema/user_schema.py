from pydantic import BaseModel
from typing import List, Optional


class Message(BaseModel):
    """return ok message"""

    message: str


class UserCreate(BaseModel):
    name: str
    email: str
    role_id: int
    team_id: int


class UserBase(BaseModel):
    """Base User scheme"""

    name: str
    email: str
    role_id: int
    guild_id: Optional[int]


class UserRequest(UserBase):
    id: Optional[int]
    password: str

    class Config:
        orm_mode = True


class UserInfo(UserBase):
    """User Info Response"""

    id: int

    class Config:
        orm_mode = True


class UserInfoAll(BaseModel):
    users: List[UserInfo]

    class Config:
        orm_mode = True
