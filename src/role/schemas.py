
from typing import List
from pydantic import BaseModel

class RoleSchema(BaseModel):
    id: int
    role: str
    
    class Config:
        from_attributes = True
        orm_mode = True