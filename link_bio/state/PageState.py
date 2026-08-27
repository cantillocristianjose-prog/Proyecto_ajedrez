import reflex as rx
from api.api import live

class PageState(rx.State):

    is_live: bool
    live_title: str

    async def check_live(self):
        live_data = await live("batmanpika1")
        self.is_live = live_data["live"]
        self.live_title = live_data["title"]