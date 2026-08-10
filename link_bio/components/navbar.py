import reflex as rx
import styles.styles as styles
from styles.colors import Color as Color
from styles.styles import Size,Spacing
import styles.styles as styles
def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "TheObsidianBoy",
            style=styles.nabvar_title_style
        ),
        position="sticky",
        bg=Color.PRIMARY.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        width="100%",
        top="0",
    )