# Punjab Real Estate ML System — Production Dockerfile
# Platform: linux/arm64 (Apple Silicon Compatible)
# Base: Python 3.11 Slim (Minimal footprint)

FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Set working directory
WORKDIR /app

# Install system dependencies
# Needed for:
# - build-essential: compiling certain python wheels
# - libgomp1: OpenMP support for certain ML libraries
# - sqlite3: MLflow tracking and inference logging
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgomp1 \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY src/ /app/src/

# Copy model artifacts and registry (Required for inference)
COPY models/ /app/models/

# Copy initial data (Optional, for demo/health checks)
COPY data/processed/ /app/data/processed/
COPY data/raw/ /app/data/raw/

# Create log directories
RUN mkdir -p /app/data/logs

# Expose FastAPI port
EXPOSE 8000

# Entrypoint: Start Inference API
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]

# --- .dockerignore recommendations ---
# .git
# .venv
# __pycache__
# .pytest_cache
# mlruns/
# .env
# tests/
# *.log
# *.db (unless pre-populating)
