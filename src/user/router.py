from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_rdb
from .service import UserService
from .schemas import UserRequest
from schemas import ResponseSchema

router = APIRouter()

@router.post("", response_model=ResponseSchema, status_code=status.HTTP_201_CREATED)
def create_user(user_request: UserRequest, db: Session = Depends(get_rdb)):
    user_service = UserService(db)

    user_response = user_service.create_user(user_request)
        
    return ResponseSchema(content = user_response)

@router.post("/login")
async def login(OAuth2_password_request_form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_rdb)):
    user_service = UserService(db)

    access_token = user_service.login_user(OAuth2_password_request_form)
        
    return ResponseSchema(content = {"access_token": access_token, "token_type": "bearer"})