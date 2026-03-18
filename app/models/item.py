from pydantic import BaseModel, Field
from typing import Optional


class TodoCreate(BaseModel):  # 요청 데이터 검증 (POST)
    title: str = Field(..., min_length=1, max_length=100, description="할 일 제목")
    done: bool = False

class TodoUpdate(BaseModel):  # 수정 데이터 검증 (PUT/PATCH)
    title: Optional[str] = Field(None, min_length=1, max_length=100, description="수정할 할 일 제목")
    done: Optional[bool] = None

class Todo(BaseModel):  # 응답 데이터 형식 정의 (JSON 직렬화) JSON으로 변환하는 것을 의미
    id: int
    title: str = Field(..., min_length=1, max_length=100, description="할 일 제목")
    done: bool = False
