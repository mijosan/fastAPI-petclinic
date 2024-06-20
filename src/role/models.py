from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database import Base
from association.associations import user_role_table

class RoleModel(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, autoincrement=True)
    role = Column(String(255), nullable=False, unique=True, index=True)
    users = relationship("UserModel", secondary=user_role_table, back_populates="roles")