# Dockerfile
FROM python:3.9.13

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app/backend

COPY . .

CMD ["python", "backend/app/main.py"]
