from typing import List, Optional
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True

class UserRequest(BaseModel):
    name: Optional[str] = None

class UserResponse(BaseModel):
    users: List[UserSchema]