from fastapi import FastAPI
import uvicorn
from routes.api import router as api_router
from src.models.users import Base
from database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        log_level="info",
        reload = True
        )