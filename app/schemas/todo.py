from pydantic import BaseModel, Field
from typing import Optional

class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="할 일 제목")
    done: bool = False


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(
        None,
        min_length=1,
        max_length=100,
        description="수정할 할 일 제목"
    )
    done: Optional[bool] = None


class Todo(BaseModel):
    id: int
    title: str
    done: bool
    user_id: int


    # ✅ 추가: SQLAlchemy ORM 객체를 Pydantic 응답으로 변환 가능하게 설정
    class Config:
        from_attributes = True
