import views.constants as const
from fastapi import FastAPI
from .TwitchAPI import TwitchAPI

TWITCH_API = TwitchAPI()


API_hello = FastAPI()

@API_hello.get("/repo")
async def repo() -> str:
    return const.REPOSITORIO_MIO

@API_hello.get("/live/{user}")
async def live(user: str) -> bool:
    return TWITCH_API.live(user)