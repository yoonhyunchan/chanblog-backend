# 베이스 이미지 (Python 3.11 최신 버전 권장)
FROM python:3.11-slim

# 작업 디렉토리 생성 및 설정
WORKDIR /app

# 의존성 복사 및 설치
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy .env file into /app
COPY .env .env
# 애플리케이션 코드 복사
COPY app ./app

# 8003 포트 노출
EXPOSE 8003

# uvicorn으로 FastAPI 실행 (실제 운영 시 gunicorn + uvicorn 워커 권장)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8003"]
