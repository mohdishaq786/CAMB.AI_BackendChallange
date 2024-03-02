import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.v1_router import router as router_v1

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_v1)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, workers=1, reload=False)
