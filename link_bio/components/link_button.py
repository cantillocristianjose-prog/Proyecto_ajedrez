import reflex as rx
import styles.styles as styles
from styles.styles import Size,Spacing

def link_button(title:str,body:str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_right",
                    width=Size.BIG.value,
                    height=Size.BIG.value,
                    margin=Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(title,style=styles.button_title_style),
                    rx.text(body,style=styles.button_body_style),
                    spacing=Spacing.VERY_SMALL.value,
                    align="start",
                    margin=Size.ZERO.value,
                ),
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )