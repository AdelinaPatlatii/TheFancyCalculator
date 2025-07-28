from app.services import nth_fibonacci, factorial, power
from app.schemas import FibonacciResponse, FactorialResponse, PowResponse
from app.models import CalculationRecord
from app.db import SessionLocal
from contextlib import contextmanager
import logging

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def fib(n: int) -> FibonacciResponse:
    result = nth_fibonacci.nth_fib(n)
    logging.info(f"Fibonacci({n}) = {result}") # logging added
    with get_db() as db:
        db.add(CalculationRecord(operation="fibonacci", input_data=f"n={n}", result=result, status_code=200))
        db.commit()
    return FibonacciResponse(result=result)


def factorial_calc(n: int) -> FactorialResponse:
    result = factorial.fact(n)
    logging.info(f"Factorial({n}) = {result}")
    with get_db() as db:
        db.add(CalculationRecord(operation="factorial", input_data=f"n={n}", result=result, status_code=200))
        db.commit()
    return FactorialResponse(result=result)


def pow(base: int, exp: int) -> PowResponse:
    result = power.power_calc(base, exp)
    logging.info(f"{base}^{exp} = {result}")
    with get_db() as db:
        db.add(CalculationRecord(operation="pow", input_data=f"base={base},exp={exp}", result=result, status_code=200))
        db.commit()
    return PowResponse(result=result)
