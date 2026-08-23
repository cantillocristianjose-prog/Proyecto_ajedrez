from fastapi import FastAPI

API_hello = FastAPI()

@API_hello.get("/hello")
def hello() -> str:
    return "TheObsidanBoy!"