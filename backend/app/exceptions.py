from fastapi import Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import ValidationError
from fastapi.responses import JSONResponse
import logging


async def unified_handler(request: Request, exc: Exception):
    if isinstance(exc, RequestValidationError):
        logging.warning(f"[VALIDATION ERROR] {exc} on {request.url}")
        return JSONResponse(
            status_code=422,
            content={"detail": "Invalid input", "errors": exc.errors()}
        )

    elif isinstance(exc, ValidationError):
        logging.warning(f"[PYDANTIC ERROR] {exc} on {request.url}")
        return JSONResponse(
            status_code=422,
            content={"detail": "Validation failed", "errors": exc.errors()}
        )

    elif isinstance(exc, StarletteHTTPException):
        logging.warning(f"[HTTP ERROR] {exc.status_code} on {request.url}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail}
        )

    else:
        logging.error(f"[UNEXPECTED ERROR] {exc} on {request.url}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error"}
        )

def register_exception_handlers(app):
    app.add_exception_handler(RequestValidationError, unified_handler)
    app.add_exception_handler(ValidationError, unified_handler)
    app.add_exception_handler(StarletteHTTPException, unified_handler)
    app.add_exception_handler(Exception, unified_handler)