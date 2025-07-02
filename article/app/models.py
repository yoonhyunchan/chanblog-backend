from sqlalchemy import Column, Integer, String, Text, Date, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(150), unique=True, nullable=False)
    title = Column(String(300), nullable=False)
    subtitle = Column(String(300))
    excerpt = Column(Text)
    intro = Column(Text)
    content = Column(Text)
    category_id = Column(Integer, nullable=False)
    date = Column(Text)
    image = Column(String(300))
    tags = Column(Text)  # You can change to ARRAY or JSONB if needed
    author_name = Column(String(100))
    author_title = Column(String(100))
    author_avatar_path = Column(String(300))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    # category = relationship("Category")  # Uncomment if Category model exists 