import reflex as rx
import styles.styles as styles
from model.Featured import Featured
from styles.styles import Size
from styles.styles import Spacing
from styles.colors import Color

def featured_link(featured: Featured) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=featured.image,
                width="100%",
                heigth="auto",
                border_radius=Size.DEFAULT.value
            ),

            rx.text(
                featured.title,
                style=styles.button_body_style
            ),
            spacing=Spacing.SMALL.value
        ),
        href=featured.url,
        is_external=True,
        _hover={}
    )

