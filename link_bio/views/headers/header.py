import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="TB", size="5")
    )