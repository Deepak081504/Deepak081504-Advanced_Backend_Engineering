from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.auth_schema import RegisterSchema, LoginSchema
from app.services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(user: RegisterSchema, db: Session = Depends(get_db)):

    new_user = register_user(db, user)

    return {
        "message": "User Registered",
        "user": new_user.email
    }


@router.post("/login")
def login(user: LoginSchema, db: Session = Depends(get_db)):

    token = login_user(db, user)

    if not token:
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    return {
        "access_token": token,
        "token_type": "bearer"
    }