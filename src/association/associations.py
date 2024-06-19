from sqlalchemy import Column, ForeignKey, String, Integer, Table
from database import Base

user_role_table = Table('user_role', Base.metadata,
    Column('user_id', String(100), ForeignKey('user.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True),
    Column('role_id', Integer, ForeignKey('role.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
)