from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import time

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        print(f"### Request: {request.method} {request.url} completed in {process_time} seconds ###")
        
        return response