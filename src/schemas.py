from enum import Enum
from typing import Any, Optional
from pydantic import BaseModel
from fastapi import FastAPI

class StatusCodeEnum(int, Enum):
    SUCCESS = 200
    ERROR = 400

class ResponseSchema(BaseModel):
    status_code: StatusCodeEnum = StatusCodeEnum.SUCCESS
    message: str = "success !"
    content: Optional[Any] = None