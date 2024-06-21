from fastapi import FastAPI
from middleware.logging_middleware import LoggingMiddleware
from user.exception_handlers import user_not_found_exception_handler
from user.search.exception_handlers import document_not_found_exception_handler
from user.exceptions import UserNotFoundException
from user.search.exceptions import DocumentNotFoundException
from user.search import router as user_search_router
from user import router as user_router
from exception_handlers import global_exception_handler

import logging
import logging.config
import os

from user.exception_handlers import invalid_credentials_exception_handler, operation_not_permitted_exception_handler, user_email_already_exists_exception_handler, user_id_already_exists_exception_handler, user_not_found_exception_handler
from user.exceptions import InvalidCredentialsException, OperationNotPermittedException, UserEmailAlreadyExistsException, UserIdAlreadyExistsException, UserNotFoundException

def create_app() -> FastAPI:    
    app = FastAPI()
    
    # 라우터 등록
    app.include_router(user_router.router, prefix="/user", tags=["user"])
    app.include_router(user_search_router.router, prefix="/search/users", tags=["user_search"])
    
    # 예외 핸들러 등록
    app.add_exception_handler(UserNotFoundException, user_not_found_exception_handler)
    app.add_exception_handler(DocumentNotFoundException, document_not_found_exception_handler)
    app.add_exception_handler(UserIdAlreadyExistsException, user_id_already_exists_exception_handler)
    app.add_exception_handler(UserEmailAlreadyExistsException, user_email_already_exists_exception_handler)
    app.add_exception_handler(InvalidCredentialsException, invalid_credentials_exception_handler)
    app.add_exception_handler(OperationNotPermittedException, operation_not_permitted_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)
        
    # 미들웨어 등록
    app.add_middleware(LoggingMiddleware)

    return app

def setup_logging():
    # 현재 파일의 디렉토리 경로를 가져옵니다.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    logging_config_path = os.path.join(current_dir, 'logging.ini')
    
    # logs 디렉터리가 존재하지 않으면 생성합니다.
    logs_dir = os.path.join(os.path.dirname(current_dir), 'logs')
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    logging.config.fileConfig(logging_config_path, disable_existing_loggers=False)