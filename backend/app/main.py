from pathlib import Path

from fastapi import FastAPI
import logging
from starlette.middleware.cors import CORSMiddleware
from app.api.routes import router
import uvicorn
from app.db import Base, engine
from fastapi.staticfiles import StaticFiles
from prometheus_fastapi_instrumentator import Instrumentator
from app.exceptions import register_exception_handlers

app = FastAPI()
app.include_router(router)

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:2025"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# added monitoring with prometheus-fastapi-instrumentator
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# added logging
log_file_path = Path("backend/app/log/requests.log")
log_file_path.parent.mkdir(parents=True, exist_ok=True)
log_file_path.touch(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("backend/app/log/requests.log"),
        logging.StreamHandler()  # prints to console
    ]
)

register_exception_handlers(app)

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2025)
