from fastapi import FastAPI
from middleware.logging_middleware import LoggingMiddleware
from src.owner.exception_handlers import owner_not_found_exception_handler, global_exception_handler
from src.owner.search.exception_handlers import document_not_found_exception_handler
from src.owner.exceptions import OwnerNotFoundException
from src.owner.search.exceptions import DocumentNotFoundException
from src.owner import router as owner_router
from src.owner.search import router as owner_search_router

app = FastAPI()
    
def create_app() -> FastAPI:
    # 라우터 등록
    app.include_router(owner_router.router, prefix="/owners", tags=["owners"])
    app.include_router(owner_search_router.router, prefix="/search/owners", tags=["owner_search"])
    
    # 예외 핸들러 등록
    app.add_exception_handler(OwnerNotFoundException, owner_not_found_exception_handler)
    app.add_exception_handler(DocumentNotFoundException, document_not_found_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)
        
    # 미들웨어 등록
    app.add_middleware(LoggingMiddleware)

    return app