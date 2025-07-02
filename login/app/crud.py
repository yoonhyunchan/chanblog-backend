from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .models import User
from .schemas import UserRegister, UserUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str) -> User:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def create_user(db: Session, user: UserRegister):
    hashed_pw = pwd_context.hash(user.password)
    new_user = User(
        email=user.email,
        hashed_password=hashed_pw,
        name=user.name,
        title=user.title,
        avatar_path=user.avatar_path
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user_info(db: Session, user: User, update_data: UserUpdate):
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)