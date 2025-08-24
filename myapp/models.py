from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    client_key = Column(String, unique=True, index=True)
    hashed_secret = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
