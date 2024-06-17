from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "user"

    id = Column(String(100), primary_key=True, index=True)
    password = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)