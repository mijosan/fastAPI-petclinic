from typing import List, Optional
from pydantic import BaseModel

class Pagination(BaseModel):
    skip: int = 0
    limit: int = 10
    
class Owner(BaseModel):
    id: int
    name: str
    
    class Config:
        orm_mode = True
        from_attributes = True

class OwnerRequest(Pagination):
    name: Optional[str] = None

class OwnerResponse(BaseModel):
    owners: List[Owner]