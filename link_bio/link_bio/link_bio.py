"""Ctrl + Shift + P y poner "Python: Select Interpreter" y seleccionar el interprete de python que diga venv"""
import reflex as rx
from components.navbar import navbar
from views.headers.header import header
from views.links.links import links
from components.footer import footer
class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer(),
        width="100%",
        border_radius="0.5rem",
        direction="column",
        align="center",
        justify="center",
    )

app = rx.App()
app.add_page(index)
