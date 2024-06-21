from fastapi import Request
from fastapi.responses import JSONResponse

from schemas import StatusCodeEnum
from .exceptions import DocumentNotFoundException

async def document_not_found_exception_handler(request: Request, exc: DocumentNotFoundException):
    return JSONResponse(
        status_code = StatusCodeEnum.CLIENT_ERROR,
        content={"message": f"Document with name: {exc.name} not found"},
    )