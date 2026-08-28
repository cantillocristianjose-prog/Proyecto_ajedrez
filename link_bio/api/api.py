import views.constants as const
from fastapi import FastAPI
from .TwitchAPI import TwitchAPI
from .SuperbaseAPI import SuperbaseAPI

TWITCH_API = TwitchAPI()
SUPABASE_API = SuperbaseAPI()

API_hello = FastAPI()

@API_hello.get("/repo")
async def repo() -> str:
    return const.REPOSITORIO_MIO

@API_hello.get("/live/{user}")
async def live(user: str) -> dict:
    return TWITCH_API.live(user)

async def featured() -> list:
    return SUPABASE_API.featured()