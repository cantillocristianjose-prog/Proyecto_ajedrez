import reflex as rx
import styles.styles as styles
def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("TheObsidianBoy"),
        position="sticky",
        bg="purple",
        padding_x=styles.MEDIUM_SIZE_Space,
        padding_y=styles.SMALL_SIZE_Space,
        z_index="999",
        width="100%",
        top="0"
    )