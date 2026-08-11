"""Ctrl + Shift + P y poner "Python: Select Interpreter" y seleccionar el interprete de python que diga venv"""
import reflex as rx
import styles.styles as styles
from styles.styles import Size
from styles.colors import Color
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
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )


app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS
)
app.add_page(
    index,
    title="TheObsidianBoy | Mi linkbiografica",
    description="Hola mi nombre es TheObsidianBoy y soy creador de contenido",
    image="foto_de_sebas.jpeg"
    )