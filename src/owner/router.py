from fastapi import APIRouter, Depends, Path, Query
from .service import OwnerService
from .schemas import OwnerRequest, OwnerResponse
from sqlalchemy.orm import Session
from database import get_rdb

router = APIRouter()

@router.get("/", response_model=OwnerResponse)
async def get_owners(
    name: str = Query(None, title="Name to search for"),
    skip: int = Query(0, ge=0, title="Number of records to skip"),
    limit: int = Query(10, ge=1, title="Maximum number of records to return"),
    db: Session = Depends(get_rdb)
):
    owner_request = OwnerRequest(name=name, skip=skip, limit=limit)
    owner_service = OwnerService(db)
    
    return owner_service.get_owners(owner_request)

@router.get("/{owner_id}", response_model=OwnerResponse)
async def get_owner(
    owner_id: int = Path(title="The ID of the item to get", ge=0, le=999999999),
    db: Session = Depends(get_rdb)
):
    owner_service = OwnerService(db)
    
    return owner_service.get_owner(owner_id)
