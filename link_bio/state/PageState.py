import reflex as rx
from api.api import live,featured

class PageState(rx.State):

    is_live: bool
    live_title: str
    featured_info: list

    async def check_live(self):
        live_data = await live("theobsidianboy")
        self.is_live = live_data["live"]
        self.live_title = live_data["titulo"]

    async def featured_links(self):
        self.featured_info = await featured()