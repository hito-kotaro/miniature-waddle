from pydantic import BaseModel, Field


class AuthRequest(BaseModel):
    email: str
    password: str


class AuthResponse(BaseModel):
    access_token: str = Field(None, example="eyjasdjsadkjsahdisabbXXXXXXXXXX")
    token_type: str = Field(None, example="bearer")
    user_id: int = Field(None, example=1)
    username: str = Field(None, example="tohi")
