from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from backend.app.api.routes import router
import uvicorn
from backend.app.db import Base, engine
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.include_router(router)

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2025)