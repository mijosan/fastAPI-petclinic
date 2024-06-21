# src/user/exception_handlers.py
from fastapi import Request
from schemas import ResponseSchema, StatusCodeEnum
from .exceptions import InvalidCredentialsException, OperationNotPermittedException, UserEmailAlreadyExistsException, UserIdAlreadyExistsException, UserNotFoundException

async def user_id_already_exists_exception_handler(request: Request, exc: UserIdAlreadyExistsException):
    return ResponseSchema(
        status_code = StatusCodeEnum.CLIENT_ERROR,
        content = {"message": f"User with ID {exc.id} already exists"},
    )
    
async def user_email_already_exists_exception_handler(request: Request, exc: UserEmailAlreadyExistsException):
    return ResponseSchema(
        status_code = StatusCodeEnum.CLIENT_ERROR,
        content = {"message": f"User with Email {exc.email} already exists"},
    )
    
async def invalid_credentials_exception_handler(request: Request, exc: InvalidCredentialsException):
    return ResponseSchema(
        status_code = StatusCodeEnum.CLIENT_ERROR,
        content={"message": exc.detail},
    )

async def operation_not_permitted_exception_handler(request: Request, exc: OperationNotPermittedException):
    return ResponseSchema(
        status_code = StatusCodeEnum.CLIENT_ERROR,
        content={"message": exc.detail},
    )
    
async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return ResponseSchema(
        status_code = StatusCodeEnum.CLIENT_ERROR,
        content={"message": f"User with ID {exc.id} not found"},
    )
