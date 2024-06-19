from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from database import Base
from association import user_role_table

class UserModel(Base):
    __tablename__ = "user"

    id = Column(String(100), primary_key=True, index=True)
    password = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    roles = relationship("role.models.RoleModel", secondary=user_role_table, back_populates="users")