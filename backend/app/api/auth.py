import logging
from datetime import datetime, timedelta
from contextlib import contextmanager
from typing import Optional
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.db import SessionLocal
from app.models import User, RequestRecord
from app.schemas import UserCreate, UserLogin
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def signup_user(input_user: UserCreate):
    hashed_pw = pwd_context.hash(input_user.password)
    with get_db() as db:
        existing = db.query(User).filter(User.username == input_user.username).first()
        if existing:
            raise HTTPException(status_code=400, detail="Username already occupied")

        new_user = User(username=input_user.username, hashed_password=hashed_pw)
        db.add(new_user)
        db.add(RequestRecord(operation="login",
                             input=f"Username={input_user.username}",
                             output="User created", status_code=200))
        db.commit()
    logging.info(f"User '{input_user.username}' added to database")
    return {"message": "User created successfully!"}


def authenticate_user(input_user: UserLogin):
    with get_db() as db:
        user = db.query(User).filter(User.username == input_user.username).first()

        if not user or not pwd_context.verify(input_user.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        db.add(RequestRecord(operation="login",
                             input=f"Username={input_user.username}",
                             output="User authenticated", status_code=200))
        db.commit()

    access_token = create_access_token(data={"sub": input_user.username})
    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: Optional[str] = payload.get("sub")
        if not username:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    with get_db() as db:
        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise credentials_exception
        return user
