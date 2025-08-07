# 🧮 The Fancy Calculator

This is a production-style **microservice** built using **FastAPI**, designed to expose mathematical operations via an HTTP API and a lightweight HTML frontend with secure user authentication.

It supports:
- Computation of the **n-th Fibonacci number**
- Computation of the **factorial** of a number
- Computation of **a<sup>b</sup>** in logarithmic time!
- Computation of **log<sub>a</sub>b**
- Computation of the **greatest common divisor** of two numbers
- Computation of the **least common multiple** of two numbers

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
│   │   ├── nth_fibonacci.py         # Fibonacci implementation + caching
│   │   ├── factorial.py             # Factorial logic + caching
│   │   ├── gcd.py                   # greatest common divisor of any two positive integers + caching
│   │   ├── lcm.py                   # least common multiple of any two positive integers + caching
│   │   ├── logarithm.py             # logarithm computation + caching
│   │   └── power.py                 # Log-time exponentiation + caching
│   ├── models.py                    # SQLAlchemy DB models
│   ├── schemas.py                   # Pydantic request/response schemas
│   ├── db.py                        # SQLite DB setup
│   ├── config.py
│   ├── exceptions.py                # Global exception handling
│   └── main.py                      # app entrypoint
├── frontend/
│   ├── calculator.html              # Calculator page
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
   
2. **Create your `.env` file based on the provided template:**
    ```bash
   cp .env.example .env
- For local development, you can use simple values like:
   ```bash
  SECRET_KEY=calculator
  ALGORITHM=HS256
  ACCESS_TOKEN_EXPIRE_MINUTES=30

3. **Make sure you have Docker Compose v2+ installed:**

    To verify:
   ```bash
   docker compose version

4. **Start the service (build + run):**
   ```bash
   docker compose up --build

5. **Visit the app in your browser:**

   http://localhost:2025
