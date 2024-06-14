import sys
import os

# 프로젝트 루트 경로를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import uvicorn
from src.app_config import create_app

app = create_app()

@app.get("/")
def read_root():
    return {"FastAPI PetClinic Sample Application"}

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
