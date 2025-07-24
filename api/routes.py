from fastapi import APIRouter, Query
from api import controllers

router = APIRouter()

@router.get("/fib", response_model=int, tags=["Fancy mathematics operations"], summary="Calculate the n-th Fibonacci number")
def fib_endpoint(n: int = Query(..., ge=0, description="Index of the Fibonacci number (must be ≥ 0 !!!!)")) -> int:
    return controllers.fib(n)
