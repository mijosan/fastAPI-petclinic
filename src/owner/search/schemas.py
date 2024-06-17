from typing import List, Optional
from pydantic import BaseModel

class OwnerSchema(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True

class OwnerRequest(BaseModel):
    name: Optional[str] = None

class OwnerResponse(BaseModel):
    owners: List[OwnerSchema]