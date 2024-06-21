
from fastapi import APIRouter, Depends, Query, status
from fastapi.params import Path
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from auth.utils import verify_token
from database import get_rdb
from .service import UserService
from .schemas import UserRequest
from schemas import ResponseSchema

router = APIRouter()

@router.post("", response_model = ResponseSchema, status_code = status.HTTP_201_CREATED)
async def create_user(user_request: UserRequest, db: Session = Depends(get_rdb)):
    user_service = UserService(db)

    user_response = user_service.create_user(user_request)
        
    return ResponseSchema(content = user_response)

@router.post("/login")
async def login(OAuth2_password_request_form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_rdb)):
    user_service = UserService(db)

    access_token = user_service.login_user(OAuth2_password_request_form)
        
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("", response_model = ResponseSchema)
async def get_users(
    id: str = Query(None, title="id to search for"),
    skip: int = Query(0, ge=0, title="Number of records to skip"),
    limit: int = Query(10, ge=1, title="Maximum number of records to return"),
    db: Session = Depends(get_rdb),
    token: str = Depends(verify_token(["admin"]))
):
    user_request = UserRequest(id = id, skip = skip, limit = limit)
    user_service = UserService(db)
    
    users = user_service.get_users(user_request)
    
    return ResponseSchema(content = users)

@router.get("/{id}", response_model = ResponseSchema)
async def get_user(
    id: str = Path(title="The ID of the item to get"),
    db: Session = Depends(get_rdb),
    token: str = Depends(verify_token(["admin"]))
):
    user_service = UserService(db)
    
    return ResponseSchema(content = user_service.get_user(id))