from pydantic import BaseModel


class Settings(BaseModel):
    PROJECT_NAME: str = "AI E-commerce MVP API"
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]


settings = Settings()

