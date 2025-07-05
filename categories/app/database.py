from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .settings import settings  # settings import

# SQLALCHEMY_DATABASE_URL = settings.sqlalchemy_database_url
DB_HOST = settings.db_host
DB_PORT = settings.db_port
DB_USER = settings.db_user
DB_PASSWORD = settings.db_password
DB_NAME = settings.db_name

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# DB_HOST=mydb.cdc88c6aktwi.us-west-2.rds.amazonaws.com
# DB_PORT=5432
# DB_USER=chan
# DB_PASSWORD=your_password_here
# DB_NAME=postgres
# SQLALCHEMY_DATABASE_URL=postgresql://chan:5372@host.docker.internal:5432/chandb

