
from typing import List
from pydantic import BaseModel

class RoleSchema(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True
        orm_mode = True