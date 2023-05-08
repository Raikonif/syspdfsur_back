from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from app.config import Base


class Book(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    gender = Column(String)


