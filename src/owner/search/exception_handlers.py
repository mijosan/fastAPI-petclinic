from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .exceptions import DocumentNotFoundException

app = FastAPI()

async def document_not_found_exception_handler(request: Request, exc: DocumentNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": f"Document with name: {exc.name} not found"},
    )