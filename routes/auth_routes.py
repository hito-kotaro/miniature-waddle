from fastapi import Depends
from sqlalchemy.orm import Session
import routes.router_base as rb
from schema import auth_schema as auth_sc
from passlib.context import CryptContext
from cruds.auth import auth_user

router = rb.create_router("auth")


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/", response_model=auth_sc.AuthResponse)
def create_access_token(request: auth_sc.AuthRequest, db: Session = Depends(rb.get_db)):
    return auth_user(request=request, db=db)
