from fastapi import APIRouter, Depends, Query

from schemas import ResponseSchema
from user.schemas import UserRequest, UserResponse
from .service import UserSearchService
from elasticsearch import Elasticsearch
from database import get_es

router = APIRouter()

@router.get("", response_model=ResponseSchema)
async def search_users(
    name: str = Query(None, title="Name to search for"),
    es: Elasticsearch = Depends(get_es)
):
    user_search_service = UserSearchService(es)
    
    user_request = UserRequest(name = name)
    
    return ResponseSchema(content = user_search_service.search_users(user_request))