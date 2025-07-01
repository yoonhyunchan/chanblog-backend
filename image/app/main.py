from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import os
import shutil
import uuid

app = FastAPI()

# CORS 설정 (필요에 따라 origin 수정)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발 시 전부 허용, 운영 시 도메인 명시 추천
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 이미지 저장 경로 (여기에 NFS가 마운트되어 있을 수도 있음)
UPLOAD_DIR = "./uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 정적 파일 서빙 (이미지 접근용)
app.mount("/static", StaticFiles(directory=UPLOAD_DIR), name="static")

@app.post("/api/upload")
async def upload_image(file: UploadFile = File(...)):
    allowed_ext = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in allowed_ext:
        raise HTTPException(status_code=400, detail="Unsupported file type.")

    filename = f"{uuid.uuid4().hex}{ext}"
    filepath = os.path.join(UPLOAD_DIR, filename)

    try:
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {e}")

    # 클라이언트가 접근할 URL 반환 (FastAPI static 경로)
    url = f"http://localhost:8003/static/{filename}"
    return {"url": url}