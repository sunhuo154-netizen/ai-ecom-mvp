from fastapi import APIRouter

from app.api.routes import ai, products

api_router = APIRouter()
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])

