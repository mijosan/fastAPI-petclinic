from sqlalchemy import Column, Integer, String
from database import Base

class OwnerModel(Base):
    __tablename__ = "owner"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)