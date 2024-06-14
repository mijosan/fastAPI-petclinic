import sys
import os

# 프로젝트 루트 경로를 sys.path에 추가
sys.path.append(os.path.dirname(__file__))

import uvicorn
from app_init import create_app, setup_logging


# 로깅 설정 초기화
setup_logging()

# FastAPI 애플리케이션 생성
app = create_app()

# 루트 라우트 설정
@app.get("/")
def read_root():
    return {"FastAPI PetClinic Sample Application"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
