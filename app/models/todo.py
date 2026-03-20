from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.db.base import Base


class TodoDB(Base):
    __tablename__ = "todo_table"   # ✅ 추가: 실제 DB 테이블명

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, unique=True, index=True)
    done = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    image_path = Column(String(255), nullable=True)



# class UserDB(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)
#     username = Column(String(50))
#     password = Column(String(255))
