from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server is starting")
    yield
    print("server is shutting down")


app = FastAPI(
    title="Book service",
    version="0.1.0",
    description="A simple example of a FastAPI application",
    # docs_url="/",
    # redoc_url="/",
    openapi_url="/openapi.json",
    lifespan=lifespan
    
)

@app.get("/")
def home():
    return {"message": "Welcome to Home Page"}


@app.get("/ping")
async def ping():
    return {"message": "Pong!!!!"}