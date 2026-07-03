from fastapi import APIRouter, HTTPException

from app.models.ai import ChatRequest, ChatResponse, GenerateRequest, GenerateResponse
from app.services.ai_service import generate_content, reply_to_chat
from app.services.product_service import get_product_by_id

router = APIRouter()


@router.post("/generate", response_model=GenerateResponse)
def generate_ai_content(payload: GenerateRequest) -> GenerateResponse:
    product = get_product_by_id(payload.product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return generate_content(product=product, tone=payload.tone)


@router.post("/chat", response_model=ChatResponse)
def ai_chat(payload: ChatRequest) -> ChatResponse:
    return reply_to_chat(payload.message)

