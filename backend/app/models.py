from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .db import Base

class CalculationRecord(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, index=True)
    input_data = Column(String)
    result = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
