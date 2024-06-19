from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from association.associations import user_role_table
from database import Base
class UserModel(Base):
    __tablename__ = "user"

    id = Column(String(100), primary_key=True, index=True)
    password = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    roles = relationship("RoleModel", secondary=user_role_table, back_populates="users")