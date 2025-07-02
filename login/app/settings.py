from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    sqlalchemy_database_url: str
    default_email: str
    default_username: str
    default_password: str
    default_title: str
    default_avatar_path: str
    
    class Config:
        env_file = ".env"

settings = Settings()