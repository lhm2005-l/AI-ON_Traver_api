from fastapi import FastAPI
from routes.travel import category
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(category.router)

origins = [
    "http://localhost:5174",
    "http://localhost:5174/*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():