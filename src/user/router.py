from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_rdb
from .service import UserService
from .schemas import UserRequest, UserResponse

router = APIRouter()

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_request: UserRequest, db: Session = Depends(get_rdb)):
    user_service = UserService(db)

    user_response = user_service.create_user(user_request)
        
    return user_response

@router.post("/login")
async def login(user_request: UserRequest, db: Session = Depends(get_rdb)):
    user_service = UserService(db)

    access_token = user_service.login_user(user_request)
        
    return {"access_token": access_token, "token_type": "bearer"}