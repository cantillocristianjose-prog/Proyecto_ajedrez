import reflex as rx
import styles.styles as styles
import views.utils as utils
from state.PageState import PageState
from routers import Route
from styles.styles import Size
from styles.colors import Color
from components.navbar import navbar
from views.header import header
from views.libros_link import libros_link
from components.footer import footer

@rx.page(
    route=Route.LIBROS.value,
    title=utils.libros_title,
    description=utils.libros_descripcion,
    image=utils.preview,
    meta=utils.videos_meta,
    on_load=PageState.check_live
)

def libros() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(
                    False,
                    PageState.live_status
                ),
                libros_link(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )

