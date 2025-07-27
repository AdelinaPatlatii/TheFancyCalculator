from backend.app.services import nth_fibonacci, factorial, power
from backend.app.schemas import FibonacciResponse, FactorialResponse, PowResponse
from backend.app.models import CalculationRecord
from backend.app.db import SessionLocal
from contextlib import contextmanager

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def fib(n: int) -> FibonacciResponse:
    result = nth_fibonacci.nth_fib(n)
    with get_db() as db:
        db.add(CalculationRecord(operation="fibonacci", input_data=f"n={n}", result=result))
        db.commit()
    return FibonacciResponse(result=result)


def factorial_calc(n: int) -> FactorialResponse:
    result = factorial.fact(n)
    with get_db() as db:
        db.add(CalculationRecord(operation="factorial", input_data=f"n={n}", result=result))
        db.commit()
    return FactorialResponse(result=result)


def pow(base: int, exp: int) -> PowResponse:
    result = power.power_calc(base, exp)
    with get_db() as db:
        db.add(CalculationRecord(operation="pow", input_data=f"base={base},exp={exp}", result=result))
        db.commit()
    return PowResponse(result=result)
