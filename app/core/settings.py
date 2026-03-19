class Settings:
    PROJECT_NAME: str = "FastAPI Todo API"
    VERSION: str = "2.2.0"
    DATABASE_URL: str = "sqlite:///./todo.db"
    ALLOWED_ORIGINS: list[str] = ["*"]

    SECRET_KEY: str = "my-super-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

# ✅ 추가: 설정 객체 생성
settings = Settings()