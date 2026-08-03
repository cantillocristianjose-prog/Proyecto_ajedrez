"""utiliza venv/Scripts/activate para activar el entorno virtual"""
import reflex as rx

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.text("Hello, Reflex!", font_size="2em", color="blue")

app = rx.App()
app.add_page(index)
