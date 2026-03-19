from app.db.base import Base
from app.db.session import engine

def init_db():
    # ✅ 순환 참조 방지를 위해 함수 내부에서 모델 임포트
    from app.models.todo import TodoDB  # noqa: F401
    
    # 테이블 생성
    Base.metadata.create_all(bind=engine)