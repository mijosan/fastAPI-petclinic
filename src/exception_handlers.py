from schemas import ResponseSchema, StatusCodeEnum
from fastapi import Request

# 전역 예외 핸들러
async def global_exception_handler(request: Request, exc: Exception):
    return ResponseSchema(
        status_code = StatusCodeEnum.SERVER_ERROR,
        content = {"message": "An unexpected error occurred"},
    )