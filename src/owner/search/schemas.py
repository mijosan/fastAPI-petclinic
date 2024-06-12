from typing import List, Optional
from pydantic import BaseModel

class Owner(BaseModel):
    id: int
    name: str
    
    class Config:
        orm_mode = True
        from_attributes = True

class OwnerRequest(BaseModel):
    name: Optional[str] = None

class OwnerResponse(BaseModel):
    owners: List[Owner]