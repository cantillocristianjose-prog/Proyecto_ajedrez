import reflex as rx
from api.api import live,featured,schedule
from model.Live import Live
from model.Featured import Featured
from views import utils

class PageState(rx.State):

    live_status = Live(live=False,title="")
    next_live: str = ""
    featured_info: list[Featured]

    async def check_live(self):
        self.live_status = True # await live("theobsidianboy")
        if not self.live_status.live:
            self.next_live = utils.next_date(await schedule())

    async def featured_links(self):
        self.featured_info = await featured()