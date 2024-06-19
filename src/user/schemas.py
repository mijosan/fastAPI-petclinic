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
        orm_mode = True

class UserRequest(Pagination):
    id: str
    password: str
    email: Optional[EmailStr] = None

class UserResponse(BaseModel):
    message: str
    users: List[UserSchema]