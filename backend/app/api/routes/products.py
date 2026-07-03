from fastapi import APIRouter

from app.models.product import Product
from app.services.product_service import get_hot_products

router = APIRouter()


@router.get("/hot", response_model=list[Product])
def hot_products() -> list[Product]:
    return get_hot_products()
