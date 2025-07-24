from fastapi import FastAPI
from api.routes import router
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import os

app = FastAPI()
app.include_router(router)

templates = Jinja2Templates(directory="templates")
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "The Fancy Calculator"})
