from fastapi import APIRouter
from src.endpoints import users, transfers

router = APIRouter()
router.include_router(users.router)
router.include_router(transfers.router)