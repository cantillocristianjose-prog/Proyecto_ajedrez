import reflex as rx
import styles.styles as styles
import views.utils as utils
from routers import Route
from styles.styles import Size
from styles.colors import Color
from components.navbar import navbar
from views.header import header
from views.index_link import index_link
from components.footer import footer

@rx.page(
        route=Route.VIDEOS.value,
        title=utils.videos_title,
        description=utils.videos_descripcion,
        image=utils.preview,
        meta=utils.videos_meta
)

def videos() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_link(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )

