from typing import List, Optional
from pydantic import BaseModel, EmailStr

class Pagination(BaseModel):
    skip: Optional[int] = 0
    limit: Optional[int] = 10
    
class UserSchema(BaseModel):
    id: str
    email: EmailStr
    
    class Config:
        from_attributes = True

class UserRequest(Pagination):
    id: str
    password: str
    email: EmailStr

class UserResponse(BaseModel):
    message: str
    users: List[UserSchema]