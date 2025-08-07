from app.services import nth_fibonacci, factorial, power, gcd, lcm, logarithm
from app.schemas import FibonacciResponse, FactorialResponse, PowResponse, \
    GCDResponse, LCMResponse, LogResponse
from app.models import RequestRecord
from app.db import SessionLocal
from contextlib import contextmanager
from fastapi import HTTPException
import logging


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def fib(n: int) -> FibonacciResponse:
    try:
        result = nth_fibonacci.nth_fib(n)
    except ValueError as e:
        logging.warning(f"[INPUT ERROR] {e}")
        raise HTTPException(status_code=400, detail=str(e))
    logging.info(f"Fibonacci({n}) = {result}")
    with get_db() as db:
        db.add(RequestRecord(operation="fibonacci", input=f"n={n}",
                             output=str(result), status_code=200))
        db.commit()
    return FibonacciResponse(result=result)


def factorial_calc(n: int) -> FactorialResponse:
    try:
        result = factorial.fact(n)
    except ValueError as e:
        logging.warning(f"[INPUT ERROR] {e}")
        raise HTTPException(status_code=400, detail=str(e))
    logging.info(f"Factorial({n}) = {result}")
    with get_db() as db:
        db.add(RequestRecord(operation="factorial", input=f"n={n}",
                             output=str(result), status_code=200))
        db.commit()
    return FactorialResponse(result=result)


def pow_calc(base: float, exp: float) -> PowResponse:
    try:
        result = power.power_calc(base, exp)
    except ValueError as e:
        logging.warning(f"[INPUT ERROR] {e}")
        raise HTTPException(status_code=400, detail=str(e))
    logging.info(f"{base}^{exp} = {result}")
    with get_db() as db:
        db.add(RequestRecord(operation="pow",
                             input=f"base={base},exp={exp}",
                             output=str(result), status_code=200))
        db.commit()
    return PowResponse(result=result)


def gcd_calc(a: int, b: int) -> GCDResponse:
    try:
        result = gcd.gcd(a, b)
    except ValueError as e:
        logging.warning(f"[INPUT ERROR] {e}")
        raise HTTPException(status_code=400, detail=str(e))
    logging.info(f"GCD({a}, {b}) = {result}")
    with get_db() as db:
        db.add(
            RequestRecord(operation="gcd", input=f"a={a},b={b}", output=result,
                          status_code=200))
        db.commit()
    return GCDResponse(result=result)


def lcm_calc(a: int, b: int) -> LCMResponse:
    try:
        result = lcm.lcm(a, b)
    except ValueError as e:
        logging.warning(f"[INPUT ERROR] {e}")
        raise HTTPException(status_code=400, detail=str(e))
    logging.info(f"LCM({a}, {b}) = {result}")
    with get_db() as db:
        db.add(
            RequestRecord(operation="lcm", input=f"a={a},b={b}",
                          output=str(result), status_code=200))
        db.commit()
    return LCMResponse(result=result)


def log_calc(base: float, value: float) -> LogResponse:
    try:
        result = logarithm.log_base(base, value)
    except ValueError as e:
        logging.warning(f"[INPUT ERROR] {e}")
        raise HTTPException(status_code=400, detail=str(e))
    logging.info(f"log base {base} of {value} = {result}")
    with get_db() as db:
        db.add(
            RequestRecord(operation="log", input=f"base={base},value={value}",
                          output=str(result), status_code=200))
        db.commit()
    return LogResponse(result=result)
