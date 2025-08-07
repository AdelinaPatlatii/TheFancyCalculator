from fastapi import APIRouter, Query
from app.api import controllers
from app.schemas import FibonacciResponse, PowResponse, FactorialResponse, \
    LogResponse, GCDResponse, LCMResponse, UserCreate, UserLogin, Token
from fastapi.responses import RedirectResponse
from app.api import auth
from app.api.auth import get_current_user
from fastapi import Depends
from app.models import User


router = APIRouter()


@router.get("/", include_in_schema=False)
def redirect_to_login():
    return RedirectResponse(url="/login")


@router.post("/signup")
def signup(user: UserCreate):
    return auth.signup_user(user)


@router.post("/login", response_model=Token)
def login(user: UserLogin):
    return auth.authenticate_user(user)


@router.get("/protected")
def protected_example(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! This route is protected."}


@router.get("/fibonacci", response_model=FibonacciResponse)
def compute_fibonacci(n: int = Query(..., ge=0)):
    return controllers.fib(n)


@router.get("/pow", response_model=PowResponse)
def compute_power(base: int = Query(...), exp: int = Query(...)):
    return controllers.pow_calc(base, exp)


@router.get("/factorial", response_model=FactorialResponse)
def compute_factorial(n: int = Query(..., ge=0)):
    return controllers.factorial_calc(n)


@router.get("/gcd", response_model=PowResponse)
def compute_power(a: int = Query(..., ge=0), b: int = Query(..., ge=0)):
    return controllers.gcd_calc(a, b)


@router.get("/lcm", response_model=PowResponse)
def compute_power(a: int = Query(..., ge=0), b: int = Query(..., ge=0)):
    return controllers.lcm_calc(a, b)


@router.get("/logarithm", response_model=LogResponse)
def compute_power(base: float = Query(...), value: float = Query(...)):
    return controllers.log_calc(base, value)
