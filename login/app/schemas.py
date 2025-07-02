from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    password: str

class UserRegister(UserLogin):
    name: str | None = None
    title: str | None = None
    avatar_path: str | None = None

class UserUpdate(BaseModel):
    name: str | None = None
    title: str | None = None
    avatar_path: str | None = None
    
class UserOut(BaseModel):
    id: int
    email: str
    name: str | None = None
    title: str | None = None
    avatar_path: str | None = None

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
