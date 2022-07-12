from pydantic import BaseModel, Field


class AuthRequest(BaseModel):
    account_id: int
    email: str
    password: str
    is_account: bool


class AuthResponse(BaseModel):
    access_token: str = Field(None, example="eyjasdjsadkjsahdisabbXXXXXXXXXX")
    token_type: str = Field(None, example="bearer")
    user_id: int = Field(None, example=1)
    username: str = Field(None, example="tohi")
