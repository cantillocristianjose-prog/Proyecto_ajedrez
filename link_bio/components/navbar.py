import reflex as rx
from styles.styles import Size,Spacing
import styles.styles as styles
def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("TheObsidianBoy"),
        position="sticky",
        bg="purple",
        margin_y=Spacing.VERY_BIG.value,
        padding_x=Spacing.BIG.value,
        padding_y=Spacing.VERY_BIG.value,
        z_index="999",
        width="100%",
        top="0"
    )