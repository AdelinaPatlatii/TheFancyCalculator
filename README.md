# 🧮 The Fancy Calculator

This is a production-style **microservice** built using **FastAPI**, designed to expose mathematical operations via an HTTP API and a lightweight HTML frontend.

It supports:
- Computation of the **n-th Fibonacci number**
- Computation of the **factorial** of a number
- Computation of **a<sup>b</sup>** in logarithmic time!

All API requests are logged, validated, cached, and persisted to a SQLite database.

---

## Features:

- FastAPI-based microservice
- Exposes an HTML frontend and REST endpoints
- Uses **Pydantic** for serialization and validation
- Caching
- Request persistence with **SQLite**
- Monitoring via Prometheus-compatible `/metrics` endpoint
- Logging
- Error handling and input validation

---

## Project Structure:
```
.
├── backend/
│   ├── api/
│   │   ├── controllers.py           # Request handlers and business logic
│   │   └── routes.py                # API routes
│   ├── services/
│   │   ├── fibonacci.py             # Fibonacci implementation + caching
│   │   ├── factorial.py             # Factorial logic + caching
│   │   └── power.py                 # Log-time exponentiation + caching
│   ├── models.py                    # SQLAlchemy DB models
│   ├── schemas.py                   # Pydantic request/response schemas
│   ├── db.py                        # SQLite DB setup
│   ├── exceptions.py                # Global exception handling
│   └── main.py                      # app entrypoint
├── frontend/
│   ├── index.html                   # Main entry page
│   ├── scripts.js                   # client-side logic
│   └── calculator.png
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # (Optional) for containerization
└── docker-compose.yml               # (Optional) for full stack orchestration
```

---

## Getting Started

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   
2. **Start the FastAPI server**
   ```bash
   uvicorn backend.main:app --reload --port 2025

2. **Visit the app in your browser**
   http://localhost:2025