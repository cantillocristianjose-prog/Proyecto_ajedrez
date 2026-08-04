"""utiliza venv/Scripts/activate para activar el entorno virtual"""
import reflex as rx
from components.navbar import navbar
from views.headers.header import header

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        header(),
        navbar(),
        width="100%",
        border_radius="0.5rem",
        direction="column",
        align="center",
        justify="center",
    )

app = rx.App()
app.add_page(index)
