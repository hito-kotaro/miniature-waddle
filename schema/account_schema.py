from pydantic import BaseModel


class AccountCreate(BaseModel):
    email: str
    password: str


class AccountInfo(BaseModel):
    id: int
    email: str
    password: str

    class Config:
        orm_mode = True


class AccountScore(BaseModel):
    user_score: int
    team_score: int
    account_score: int
