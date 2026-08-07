"""Ctrl + Shift + P y poner "Python: Select Interpreter" y seleccionar el interprete de python que diga venv"""
import reflex as rx
from styles.styles import BASE_STYLE, MAX_WIDTH,Size,Spacing
from components.navbar import navbar
from views.headers.header import header
from views.links.links import links
from components.footer import footer


class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=MAX_WIDTH,
                width="100%",
                padding_x=Size.LARGE.value,
                padding_y=Size.BIG.value,
                border_radius="0.5rem",
                direction="column",
                align="center",
                justify="center",
            )
        ),
        footer(),
    )


app = rx.App(
    style=BASE_STYLE
)
app.add_page(index)
