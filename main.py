# from tc_auth.auth import Auth
from fastapi.middleware.cors import CORSMiddleware
from connect import auth 
from fastapi import FastAPI
from config import config


app = FastAPI()


auth.include_routes(app=app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



def run():
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=config.PORT,
        reload=False,
    )

if __name__ == "__main__":
    auth.init()
    run()

