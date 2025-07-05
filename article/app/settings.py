from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # sqlalchemy_database_url: str
    db_host: str
    db_port: str
    db_user: str
    db_password: str
    db_name: str
    class Config:
        env_file = ".env"

settings = Settings()
