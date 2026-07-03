from app.data.mock_products import MOCK_PRODUCTS
from app.models.product import Product


def get_hot_products() -> list[Product]:
    return MOCK_PRODUCTS


def get_product_by_id(product_id: int) -> Product | None:
    return next((product for product in MOCK_PRODUCTS if product.id == product_id), None)

