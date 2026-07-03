from app.models.ai import GenerateResponse, ChatResponse
from app.models.product import Product


def generate_content(product: Product, tone: str) -> GenerateResponse:
    tone_prefix = tone.strip().title() if tone.strip() else "Friendly"

    return GenerateResponse(
        product_id=product.id,
        title=f"{tone_prefix} launch copy for {product.name}",
        tagline=f"Make every day easier with {product.name}.",
        description=(
            f"{product.name} is built for shoppers who want practical design without giving up style. "
            f"It highlights {', '.join(product.tags)} benefits and delivers a polished experience at ${product.price:.2f}."
        ),
        social_caption=(
            f"Meet {product.name}: {product.description} "
            f"Rated {product.rating}/5 by early fans. #AIEcommerce #ProductLaunch"
        ),
    )


def reply_to_chat(message: str) -> ChatResponse:
    normalized = message.strip()
    topic = normalized if normalized else "your product"

    return ChatResponse(
        reply=f"I can help create product copy, ad angles, and buyer-focused messaging for: {topic}",
        suggestions=[
            "Generate a product description",
            "Create three ad hooks",
            "Write a short social caption",
        ],
    )

