import reflex as rx
from api.api import live,featured,schedule
from model.Live import Live
from model.Featured import Featured

class PageState(rx.State):

    live_status = Live(live=False,title="")
    featured_info: list[Featured]

    async def check_live(self):
        self.live_status = await live("theobsidianboy")
        if not self.live_status.live:
             await schedule()

    async def featured_links(self):
        self.featured_info = await featured()