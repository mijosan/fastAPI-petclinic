import sys
import os

# src 디렉토리를 sys.path에 추가
sys.path.append(os.path.join(os.path.dirname(__file__)))

import uvicorn
from .app_config import create_app

app = create_app()

@app.get("/")
def read_root():
    return {"FastAPI PetClinic Sample Application"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)