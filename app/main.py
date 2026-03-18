from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes.item import router as item_router

from app.database import engine, Base
from app.models.todo import TodoDB


# ✅ 추가: 앱 시작 시 테이블 생성
Base.metadata.create_all(bind=engine)


app = FastAPI(title="FastAPI Todo API",                 # ✅ 문서 제목 추가
    description="FastAPI, SQLalchemy 기반 Todo CRUD API",  # ✅ 문서 설명 추가
    version="2.0.0")

# ✅ 추가: CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # 학습용: 모든 출처 허용
    allow_credentials=True,       # 쿠키/인증정보 포함 허용
    allow_methods=["*"],          # 모든 HTTP 메서드 허용
    allow_headers=["*"],          # 모든 헤더 허용
)


app.include_router(item_router)

# ✅ 추가: static 폴더 연결
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def todo_page(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )    

# @app.get("/")
# def home():
#     return {"message": "FastAPI Todo API 실행 중"}



# ✅ 추가: 요청 데이터 검증 실패 시 에러 메시지 통일
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "message": "입력값 검증에 실패했습니다.",
            "errors": exc.errors()
        }
    )