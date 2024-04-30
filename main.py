from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from dotenv import dotenv_values
from pymongo import MongoClient
from routes.api import router as api_router

config = dotenv_values(".env")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("INFO:     Connecting to database...")
    app.mongodb_client = MongoClient(config["MONGO_CONNECTION_STRING"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("INFO:     Project connected to the MongoDB database!")
    yield
    # Shutdown
    app.mongodb_client.close()
    print("INFO:     Database disconnected.")

app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        log_level="info",
        reload = True
        )