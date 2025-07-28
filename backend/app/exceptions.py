from fastapi import Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import ValidationError
from fastapi.responses import JSONResponse
from app.db import SessionLocal
from app.models import CalculationRecord
from datetime import datetime
import logging

def log_error_to_db(operation: str, input_data: str, message: str, status_code: int):
    db = SessionLocal()
    try:
        record = CalculationRecord(
            operation=operation,
            input_data=input_data,
            result=None,
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
            data = await request.form()
        elif request.method == "GET":
            data = dict(request.query_params)
        else:
            data = {}
    except Exception:
        data = {}

    input_data = "Input data is either None or Empty"
    if data:
        input_data_dict = dict(data)
        if 'n' in input_data_dict:
            input_data = f"n={dict(data)['n']}"
        elif 'base' in input_data_dict and 'exp' in input_data_dict:
            input_data = f"base={dict(data)['base']},exp={dict(data)['exp']}"
        else:
            input_data = f"Idk what this is: " + str(dict(data))

    if isinstance(exc, RequestValidationError):
        msg = "Invalid input"
        logging.warning(f"[VALIDATION ERROR] {exc} on {request.url}")
        log_error_to_db(operation, input_data, msg, 422)
        return JSONResponse(status_code=422, content={"detail": msg, "errors": exc.errors()})

    elif isinstance(exc, ValidationError):
        msg = "Validation failed"
        logging.warning(f"[PYDANTIC ERROR] {exc} on {request.url}")
        log_error_to_db(operation, input_data, msg, 422)
        return JSONResponse(status_code=422, content={"detail": msg, "errors": exc.errors()})

    elif isinstance(exc, StarletteHTTPException):
        msg = exc.detail
        logging.warning(f"[HTTP ERROR] {exc.status_code} on {request.url}")
        log_error_to_db(operation, input_data, msg, exc.status_code)
        return JSONResponse(status_code=exc.status_code, content={"detail": msg})

    else:
        msg = str(exc)
        logging.error(f"[UNEXPECTED ERROR] {exc} on {request.url}")
        log_error_to_db(operation, input_data, msg, 500)
        return JSONResponse(status_code=500, content={"detail": "Internal server error"})


def register_exception_handlers(app):
    app.add_exception_handler(RequestValidationError, unified_handler)
    app.add_exception_handler(ValidationError, unified_handler)
    app.add_exception_handler(StarletteHTTPException, unified_handler)
    app.add_exception_handler(Exception, unified_handler)
