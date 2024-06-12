from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .exceptions import OwnerNotFoundException

app = FastAPI()

async def owner_not_found_exception_handler(request: Request, exc: OwnerNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": f"Owner with ID {exc.owner_id} not found"},
    )
    
# 전역 예외 핸들러
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred"},
    )