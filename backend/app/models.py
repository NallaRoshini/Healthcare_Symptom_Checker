from sqlalchemy import Column, Integer, Text, DateTime
from datetime import datetime
from .database import Base

class QueryHistory(Base):
    __tablename__ = "query_history"
    id = Column(Integer, primary_key=True, index=True)
    input_text = Column(Text)
    response_text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
