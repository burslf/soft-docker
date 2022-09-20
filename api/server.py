import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from api.routers.routes import router
from helpers.load_env import load_environment_variables

load_environment_variables(env="develop", parent_level=0)

app = FastAPI()

origins = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=router)

if __name__ == '__main__':
    uvicorn.run("api.server:app", host='127.0.0.1', port=8000, log_level="info", reload=True)
    print("running")