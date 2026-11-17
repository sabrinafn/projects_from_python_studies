from sqlalchemy import Column, Integer, String
from.database import Base

class Item(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True, nullable=False)
    created_at = Column(String, nullable=False)