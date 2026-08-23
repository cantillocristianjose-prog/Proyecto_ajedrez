import reflex as rx
from api.api import live

class PageState(rx.State):

    is_live: bool

    async def check_live(self) -> bool:
        self.is_live = await live("sebastian")