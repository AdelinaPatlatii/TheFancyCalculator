from api import controllers
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="templates")
@router.get("/fib")
def home(request: Request):
    return templates.TemplateResponse("fibonacci.html", {"request": request, "title": "Calculate the n-th Fibonacci number"})


@router.post("/fib", response_class=HTMLResponse)
async def compute_fib(request: Request, n: int = Form(...)):
    result = controllers.fib(n)
    return templates.TemplateResponse(
        "fibonacci.html",
        {
            "request": request,
            "n": n,
            "fib_result": result
        }
    )
