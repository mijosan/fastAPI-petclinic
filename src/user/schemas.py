from typing import List, Optional
from pydantic import BaseModel, EmailStr
from role.schemas import RoleSchema

class Pagination(BaseModel):
    skip: Optional[int] = 0
    limit: Optional[int] = 10

class UserSchema(BaseModel):
    id: str
    email: Optional[EmailStr] = None
    roles: List[RoleSchema] = []

    class Config:
        from_attributes=True

class UserRequest(Pagination):
    id: Optional[str] = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None

class UserResponse(BaseModel):
    message: Optional[str] = None
    users: List[UserSchema]