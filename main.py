from fastapi import FastAPI
from api.routes import router
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import os
import uvicorn

app = FastAPI()
app.include_router(router)

# static stuff mounted
app.mount("/static", StaticFiles(directory="static"), name="static")

# template rendering
templates = Jinja2Templates(directory="templates")
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "The Fancy Calculator"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2025)