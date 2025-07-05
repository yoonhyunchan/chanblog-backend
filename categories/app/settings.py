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

# DB_HOST=mydb.cdc88c6aktwi.us-west-2.rds.amazonaws.com
# DB_PORT=5432
# DB_USER=chan
# DB_PASSWORD=your_password_here
# DB_NAME=postgres