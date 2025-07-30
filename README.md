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
├── Dockerfile
└── docker-compose.yml
```


---

## Features

- FastAPI backend with REST endpoints
- HTML + JavaScript frontend UI
- SQLite persistence of all requests and errors
- Exception handling with error logging to database and logs
- Prometheus monitoring on `/metrics`
- Redis-based caching (optional)
- Docker-ready setup

---

## Database Setup

This project uses **SQLite** to persist all API requests, results, and errors.

- The database file `calculator.db` is **automatically created on first run** — no manual setup is needed.
- It stores:
  - Operation name (e.g., `"fibonacci"`, `"pow"`)
  - Input parameters (e.g., `"n=5"`)
  - Result (or `null` if there was an error)
  - Error message (if any)
  - HTTP status code (e.g., `200`, `422`)
  - Timestamp

To inspect the DB manually, run the following command:
<pre> sqlite3 calculator.db </pre>

---

## Running the App (with Docker Compose)

1. **Clone the repository and navigate to the directory** `TheFancyCalculator`:
    ```bash
   git clone https://github.com/AdelinaPatlatii/TheFancyCalculator.git
   cd TheFancyCalculator

2. **Make sure you have Docker Compose v2+ installed**
   
3. **Start the service (build + run):**
   ```bash
   docker compose up --build

4. **Visit the app in your browser:**
   http://localhost:2025
