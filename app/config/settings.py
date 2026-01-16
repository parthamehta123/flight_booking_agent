from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Flight Booking Agent"
    chroma_path: str = "./chroma"

    class Config:
        env_file = ".env"


settings = Settings()
