from typing import List, Optional
from pydantic import BaseModel

class Pagination(BaseModel):
    skip: Optional[int] = 0
    limit: Optional[int] = 10
    
class OwnerSchema(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True

class OwnerRequest(Pagination):
    name: Optional[str] = None

class OwnerResponse(BaseModel):
    owners: List[OwnerSchema]