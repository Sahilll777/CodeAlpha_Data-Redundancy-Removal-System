from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    email = Column(String, index=True)
    content = Column(String)
    hash = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)