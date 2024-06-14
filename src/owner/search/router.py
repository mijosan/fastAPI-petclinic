from fastapi import APIRouter, Depends, Query
from .schemas import OwnerRequest, OwnerResponse
from .service import OwnerSearchService
from elasticsearch import Elasticsearch
from database import get_es

router = APIRouter()

@router.get("/", response_model=OwnerResponse)
async def search_owners(
    name: str = Query(None, title="Name to search for"),
    es: Elasticsearch = Depends(get_es)
):
    owner_search_service = OwnerSearchService(es)
    
    owner_request = OwnerRequest(name=name)
    
    return owner_search_service.search_owners(owner_request)