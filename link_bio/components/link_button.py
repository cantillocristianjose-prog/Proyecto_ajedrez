import reflex as rx

def link_button(text:str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_right"
                ),
                rx.text(text)
            )
        ),
        href=url,
        is_external=True,
        width="100%"
        )