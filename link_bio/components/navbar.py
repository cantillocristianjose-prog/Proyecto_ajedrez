import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("TheObsidianBoy",height="40px"),
        position="sticky",
        bg="purple",
        padding_x="16px",
        padding_y="8px",
        z_index="999",
        width="100%",
    )