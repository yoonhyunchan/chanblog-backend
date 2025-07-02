from .settings import settings  # settings import
from . import models
from passlib.context import CryptContext
from .database import SessionLocal

DEFAULT_EMAIL = settings.default_email
DEFAULT_PASSWORD = settings.default_password
DEFAULT_USERNAME = settings.default_username
DEFAULT_TITLE = settings.default_title
DEFAULT_AVATAR_PATH = settings.default_avatar_path



def init_db():
    db = SessionLocal()
    try:
        # categories 테이블 비어있을 때만 초기 데이터 삽입
        if db.query(models.User).count() == 0:
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            default_hashed_password = pwd_context.hash(DEFAULT_PASSWORD)
            users = [
                models.User(email=DEFAULT_EMAIL, hashed_password=default_hashed_password, name=DEFAULT_USERNAME, title=DEFAULT_TITLE, avatar_path=DEFAULT_AVATAR_PATH),
            ]
            db.add_all(users)
            db.commit()
    finally:
        db.close()
