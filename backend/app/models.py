from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from .db import Base

class RequestRecord(Base):
    __tablename__ = "http_requests"

    cid = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, ForeignKey("users.uid"), nullable=True)
    operation = Column(String, index=True)
    input = Column(String)
    output = Column(String, nullable=True)
    error_message = Column(String, nullable=True)
    status_code = Column(Integer, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

