from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    base_url: str
    static_url_path: str = "/static"  # 기본값도 가능

    class Config:
        env_file = ".env"

settings = Settings()