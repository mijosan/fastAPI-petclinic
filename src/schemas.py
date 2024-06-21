from enum import Enum
from typing import Any, Optional
from pydantic import BaseModel

class StatusCodeEnum(int, Enum):
    SUCCESS = 200
    CLIENT_ERROR = 400
    SERVER_ERROR = 500

class ResponseSchema(BaseModel):
    status_code: StatusCodeEnum = StatusCodeEnum.SUCCESS
    message: str = "success !"
    content: Optional[Any] = None