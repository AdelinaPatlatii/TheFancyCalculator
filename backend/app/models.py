from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from .db import Base

class CalculationRecord(Base):
    __tablename__ = "calculations"

    cid = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, ForeignKey("users.uid"), nullable=True)
    operation = Column(String, index=True)
    input_data = Column(String)
    result = Column(Float, nullable=True)
    error_message = Column(String, nullable=True)
    status_code = Column(Integer, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

