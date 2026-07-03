from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    product_id: int
    tone: str = Field(default="friendly", examples=["friendly", "luxury", "playful"])


class GenerateResponse(BaseModel):
    product_id: int
    title: str
    tagline: str
    description: str
    social_caption: str


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str
    suggestions: list[str]

