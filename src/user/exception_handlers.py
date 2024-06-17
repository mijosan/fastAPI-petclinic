# src/user/exception_handlers.py
from fastapi import Request
from fastapi.responses import JSONResponse
from .exceptions import UserEmailAlreadyExistsException, UserIdAlreadyExistsException

async def user_id_already_exists_exception_handler(request: Request, exc: UserIdAlreadyExistsException):
    return JSONResponse(
        status_code=400,
        content={"message": f"User with ID {exc.id} already exists"},
    )
    
async def user_email_already_exists_exception_handler(request: Request, exc: UserEmailAlreadyExistsException):
    return JSONResponse(
        status_code=400,
        content={"message": f"User with Email {exc.email} already exists"},
    )