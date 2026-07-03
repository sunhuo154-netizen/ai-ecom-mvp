from app.models.product import Product


MOCK_PRODUCTS: list[Product] = [
    Product(
        id=1,
        name="Aurora Smart Desk Lamp",
        description="A dimmable desk lamp with focus, reading, and ambient modes.",
        price=79.0,
        image_url="https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=900&q=80",
        tags=["home office", "lighting", "smart"],
        rating=4.8,
    ),
    Product(
        id=2,
        name="PulseFit Wireless Earbuds",
        description="Sweat-resistant earbuds with active noise reduction and rich bass.",
        price=129.0,
        image_url="https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?auto=format&fit=crop&w=900&q=80",
        tags=["audio", "fitness", "wireless"],
        rating=4.6,
    ),
    Product(
        id=3,
        name="Nomad Travel Backpack",
        description="A lightweight carry-on backpack with modular storage and laptop protection.",
        price=149.0,
        image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=900&q=80",
        tags=["travel", "bags", "work"],
        rating=4.9,
    ),
    Product(
        id=4,
        name="BrewMate Cold Brew Kit",
        description="A compact glass cold brew maker designed for smooth coffee at home.",
        price=45.0,
        image_url="https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=900&q=80",
        tags=["coffee", "kitchen", "lifestyle"],
        rating=4.7,
    ),
]

