import uvicorn
from .app_config import create_app

app = create_app()

@app.get("/")
def read_root():
    return {"FastAPI PetClinic Sample Application"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)