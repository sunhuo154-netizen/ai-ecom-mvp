from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image_url: str
    tags: list[str]
    rating: float

