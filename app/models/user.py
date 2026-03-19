from sqlalchemy import Column, Integer, String
from app.db.base import Base

class UserDB(Base):
    __tablename__ = "users"   # ✅ 추가: users 테이블 생성

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)  
    