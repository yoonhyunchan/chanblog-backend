# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy your FastAPI app code
COPY app ./app

# Expose FastAPI port
EXPOSE 8002

# Start FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]
