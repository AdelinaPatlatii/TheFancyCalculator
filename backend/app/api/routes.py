from fastapi import APIRouter, Query
from controllers import fib, pow, factorial_calc
from ..schemas import FibonacciResponse, PowResponse, FactorialResponse

router = APIRouter()

@router.get("/fibonacci", response_model=FibonacciResponse)
def compute_fibonacci(n: int = Query(..., ge=0)):
    return controllers.fib(n)

@router.get("/pow", response_model=PowResponse)
def compute_power(base: int = Query(...), exp: int = Query(...)):
    return controllers.pow(base, exp)

@router.get("/factorial", response_model=FactorialResponse)
def compute_factorial(n: int = Query(..., ge=0)):
    return controllers.factorial_calc(n)
