import views.constants as const
from fastapi import FastAPI

API_hello = FastAPI()

@API_hello.get("/repo")
def repo() -> str:
    return const.REPOSITORIO_MIO