import reflex as rx
import styles.styles as styles

def link_icon(url:str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="compass"
        ),
        href=url,
        is_external=True,
    )