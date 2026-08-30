import views.constants as const
from fastapi import FastAPI
from .TwitchAPI import TwitchAPI
from .SuperbaseAPI import SuperbaseAPI
from model.Live import Live
from model.Featured import Featured

TWITCH_API = TwitchAPI()
SUPABASE_API = SuperbaseAPI()

API_hello = FastAPI()

@API_hello.get("/repo")
async def repo() -> str:
    return const.REPOSITORIO_MIO

@API_hello.get("/live/{user}")
async def live(user: str) -> Live:
    return TWITCH_API.live(user)

async def featured() -> list[Featured]:
    return SUPABASE_API.featured()