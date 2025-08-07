from app.services import nth_fibonacci, factorial, power, gcd, lcm, logarithm
from app.schemas import FibonacciResponse, FactorialResponse, PowResponse, \
    GCDResponse, LCMResponse, LogResponse
from app.models import RequestRecord
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
    logging.info(f"Fibonacci({n}) = {result}")
    with get_db() as db:
        db.add(RequestRecord(operation="fibonacci", input=f"n={n}",
                             output=result, status_code=200))
        db.commit()
    return FibonacciResponse(result=result)


def factorial_calc(n: int) -> FactorialResponse:
    result = factorial.fact(n)
    logging.info(f"Factorial({n}) = {result}")
    with get_db() as db:
        db.add(RequestRecord(operation="factorial", input=f"n={n}",
                             output=result, status_code=200))
        db.commit()
    return FactorialResponse(result=result)


def pow_calc(base: int, exp: int) -> PowResponse:
    result = power.power_calc(base, exp)
    logging.info(f"{base}^{exp} = {result}")
    with get_db() as db:
        db.add(RequestRecord(operation="pow",
                             input=f"base={base},exp={exp}",
                             output=result, status_code=200))
        db.commit()
    return PowResponse(result=result)


def gcd_calc(a: int, b: int) -> GCDResponse:
    result = gcd.gcd(a, b)
    logging.info(f"GCD({a}, {b}) = {result}")
    with get_db() as db:
        db.add(
            RequestRecord(operation="gcd", input=f"a={a},b={b}", output=result,
                          status_code=200))
        db.commit()
    return GCDResponse(result=result)


def lcm_calc(a: int, b: int) -> LCMResponse:
    result = lcm.lcm(a, b)
    logging.info(f"LCM({a}, {b}) = {result}")
    with get_db() as db:
        db.add(
            RequestRecord(operation="lcm", input=f"a={a},b={b}", output=result,
                          status_code=200))
        db.commit()
    return LCMResponse(result=result)


def log_calc(base: float, value: float) -> LogResponse:
    result = logarithm.log_base(base, value)
    logging.info(f"log base {base} of {value} = {result}")
    with get_db() as db:
        db.add(
            RequestRecord(operation="log", input=f"base={base},value={value}",
                          output=result, status_code=200))
        db.commit()
    return LogResponse(result=result)
