import os
import uuid
import shutil
from fastapi import UploadFile, HTTPException

from app.core.settings import settings


def ensure_upload_dir():
    os.makedirs(settings.TODO_UPLOAD_DIR, exist_ok=True)


def validate_image_file(upload_file: UploadFile):
    allowed_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp"]

    _, ext = os.path.splitext(upload_file.filename.lower())

    if ext not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="이미지 파일은 jpg, jpeg, png, gif, webp 형식만 업로드할 수 있습니다."
        )


def save_uploaded_image(upload_file: UploadFile) -> str:
    ensure_upload_dir()
    validate_image_file(upload_file)

    _, ext = os.path.splitext(upload_file.filename.lower())
    unique_filename = f"{uuid.uuid4().hex}{ext}"

    save_path = os.path.join(settings.TODO_UPLOAD_DIR, unique_filename)

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    # ✅ DB에는 상대경로 저장
    return f"/media/todos/{unique_filename}"



def delete_uploaded_file(file_url: str | None):
    if not file_url:
        return

    # 예: /media/todos/abc.png -> media/todos/abc.png
    local_path = file_url.lstrip("/")

    if os.path.exists(local_path):
        os.remove(local_path)
        
