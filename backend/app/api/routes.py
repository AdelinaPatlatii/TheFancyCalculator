# from backend.app.api import controllers
# from fastapi import APIRouter, Request, Form
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
#
#
# router = APIRouter()
# templates = Jinja2Templates(directory="templates")
# @router.get("/fib")
# def home(request: Request):
#     return templates.TemplateResponse("fibonacci.html", {"request": request, "title": "Calculate the n-th Fibonacci number"})
#
#
# @router.post("/fib", response_class=HTMLResponse)
# async def compute_fib(request: Request, n: int = Form(...)):
#     result = controllers.fib(n)
#     return templates.TemplateResponse(
#         "fibonacci.html",
#         {
#             "request": request,
#             "n": n,
#             "fib_result": result
#         }
#     )
from fastapi import APIRouter, Query
from backend.app.api import controllers
from backend.app.schemas import FibonacciResponse, PowResponse, FactorialResponse

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
