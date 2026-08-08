import reflex as rx
import styles.styles as styles
from styles.styles import Size,Spacing

def link_button(title:str,body:str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_right",
                    width=Spacing.LARGE.value,
                    height=Spacing.MEDIUM_BIG.value
                ),
                rx.vstack(
                    rx.text(title,style=styles.button_title_style),
                    rx.text(body,style=styles.button_body_style),
                    align="start",
                )
            )
        ),
        href=url,
        is_external=True,
        width="100%"
        )