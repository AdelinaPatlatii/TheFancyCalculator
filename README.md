# 🧮 The Fancy Calculator

This is a production-style **microservice** built using **FastAPI**, designed to expose mathematical operations via an HTTP API and a lightweight HTML frontend with secure user authentication.

It supports:
- Computation of the **n-th Fibonacci number**
- Computation of the **factorial** of a number
- Computation of **a<sup>b</sup>** in logarithmic time!

All API requests are logged, validated, cached, and persisted to a SQLite database.

---

## Features:

- FastAPI backend with REST endpoints
- HTML + JavaScript frontend UI
- JWT authentication using `python-jose`
- Signup/Login UI
- SQLite persistence of all requests and errors
- Exception handling with custom database logging
- Prometheus monitoring on `/metrics`
- Dictionary-based caching
- Docker-ready setup

---

## Project Structure:
```
.
├── backend/
│   ├── api/
│   │   ├── controllers.py           # Request handler for the calculator page
│   │   ├── auth.py                  # Request handler for the login/signup pages
│   │   └── routes.py                # API routes
│   ├── services/
│   │   ├── fibonacci.py             # Fibonacci implementation + caching
│   │   ├── factorial.py             # Factorial logic + caching
│   │   └── power.py                 # Log-time exponentiation + caching
│   ├── models.py                    # SQLAlchemy DB models
│   ├── schemas.py                   # Pydantic request/response schemas
│   ├── db.py                        # SQLite DB setup
│   ├── config.py
│   ├── exceptions.py                # Global exception handling
│   └── main.py                      # app entrypoint
├── frontend/
│   ├── index.html                   # Calculator page
│   ├── calculator.js                # Client-side logic for the calculator page
│   ├── login.html                   # Login page
│   ├── login.js                     # Client-side logic for the login page
│   ├── signup.html                  # Signup page
│   └── calculator_image.png
├── requirements.txt                 # Python dependencies
├── Dockerfile
└── docker-compose.yml
```


---

## Database Setup

This project uses **SQLite** to persist all API requests, results, and errors.

- The database file `calculator.db` is **automatically created on first run** — no manual setup is needed.
- It stores:
  - Operation names (e.g., `"fibonacci"`, `"pow"`)
  - Input parameters (e.g., `"n=5"`)
  - Outputs (or `null` if there was an error)
  - Error messages (if any)
  - HTTP status code (e.g., `200`, `422`)
  - Timestamps

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
