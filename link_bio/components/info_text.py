import reflex as rx
from styles.styles import Size,Spacing

def info_text(title:str,body: str) -> rx.Component:
    return rx.box(
        rx.text(title,color_scheme="blue",weight="bold",as_="span"),
        f"{body}", font_size=Spacing.SMALL.value
    )