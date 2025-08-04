import logging
from app.models import User
from app.db import SessionLocal
from passlib.context import CryptContext
from fastapi import HTTPException
from contextlib import contextmanager
from app.schemas import UserCreate, UserLogin

from app.models import CalculationRecord


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def signup_user(input_user: UserCreate):
    hashed_pw = pwd_context.hash(input_user.password)
    with get_db() as db:
        existing = db.query(User).filter(
            User.username == input_user.username).first()
        if existing:
            raise HTTPException(status_code=400,
                                detail="Username already occupied")
        db.add(User(username=input_user.username, hashed_password=hashed_pw))
        db.add(CalculationRecord(operation="login",
                                 error_message=f"User {input_user.username} "
                                               + "created", status_code=200))
        db.commit()
    logging.info(f"User added to database")
    return {"message": "User created successfully!"}


def authenticate_user(input_user: UserLogin):
    with get_db() as db:
        user = db.query(User).filter(
            User.username == input_user.username).first()

    if not user or not pwd_context.verify(input_user.password,
                                          user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    logging.info(f"User authenticated")
    db.add(CalculationRecord(operation="login",
                             error_message=f"User {input_user.username} "
                                           + "authenticated", status_code=200))
    db.commit()
    return {"message": "User authenticated!"}
