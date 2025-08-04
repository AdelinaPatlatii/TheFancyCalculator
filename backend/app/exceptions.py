from fastapi import Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import ValidationError
from fastapi.responses import JSONResponse
from app.db import SessionLocal
from app.models import RequestRecord
from datetime import datetime
import logging


def log_error_to_db(operation: str, input_data: str, message: str,
                    status_code: int):
    db = SessionLocal()
    try:
        record = RequestRecord(
            operation=operation,
            input=input_data,
            output=None,
            error_message=message,
            status_code=status_code,
            timestamp=datetime.utcnow()
        )
        db.add(record)
        db.commit()
    except Exception as e:
        logging.error(f"[DB ERROR LOGGING FAILED] {e}")
    finally:
        db.close()


async def unified_handler(request: Request, exc: Exception):
    operation_path = request.url.path
    operation = operation_path[1:]
    try:
        if request.method == "POST":
            try:
                content_type = request.headers.get("content-type", "").lower()
                if "application/json" in content_type:
                    data = await request.json()
                elif "application/x-www-form-urlencoded" in content_type or \
                        "multipart/form-data" in content_type:
                    data = await request.form()
                else:
                    data = {}
            except Exception:
                data = {}
        elif request.method == "GET":
            data = dict(request.query_params)
        else:
            data = {}
    except Exception:
        data = {}
    print(data)
    input_data = "Input data is either None or Empty"
    if data:
        input_data_dict = dict(data)
        if 'n' in input_data_dict:
            input_data = f"n={input_data_dict['n']}"
        elif 'base' in input_data_dict and 'exp' in input_data_dict:
            input_data = f"base={input_data_dict['base']},exp={input_data_dict['exp']}"
        elif 'username' in input_data_dict:
            input_data = f"username={input_data_dict['username']}"
        else:
            input_data = "Other input: " + str(input_data_dict)

    if isinstance(exc, RequestValidationError):
        msg = "Invalid input"
        logging.warning(f"[VALIDATION ERROR] {exc} on {request.url}")
        log_error_to_db(operation, input_data, msg, 422)
        return JSONResponse(status_code=422, content={"detail": msg,
                                                      "errors": exc.errors()})

    elif isinstance(exc, ValidationError):
        msg = "Validation failed"
        logging.warning(f"[PYDANTIC ERROR] {exc} on {request.url}")
        log_error_to_db(operation, input_data, msg, 422)
        return JSONResponse(status_code=422, content={"detail": msg,
                                                      "errors": exc.errors()})

    elif isinstance(exc, StarletteHTTPException):
        status = exc.status_code
        msg = exc.detail

        if status == 401:
            msg = "Invalid credentials"
        elif status == 409:
            msg = "Username already taken"

        logging.warning(f"[HTTP ERROR] {status} on {request.url} — {msg}")
        log_error_to_db(operation, input_data, msg, status)
        return JSONResponse(status_code=status, content={"detail": msg})

    else:
        msg = str(exc)
        logging.error(f"[UNEXPECTED ERROR] {exc} on {request.url}")
        log_error_to_db(operation, input_data, msg, 500)
        return JSONResponse(status_code=500,
                            content={"detail": "Internal server error"})


def register_exception_handlers(app):
    app.add_exception_handler(RequestValidationError, unified_handler)
    app.add_exception_handler(ValidationError, unified_handler)
    app.add_exception_handler(StarletteHTTPException, unified_handler)
    app.add_exception_handler(Exception, unified_handler)
