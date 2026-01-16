from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]  # project root


class Settings(BaseSettings):
    # App
    app_name: str = "Flight Booking Agent"

    # LLM
    openai_api_key: str | None = None

    # Storage
    chroma_path: str = "./chroma"

    # Database
    use_postgres: bool = False
    database_url: str | None = None

    # Security
    api_token: str = "dev-token"  # safe default for dev

    # Rate limiting
    rate_limit: str = "5/minute"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="allow",
    )


settings = Settings()
