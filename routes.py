from fastapi import APIRouter
from controllers import auth

router = APIRouter()
router.include_router(auth.router)