import reflex as rx
import datetime
from styles.colors import TextColor as TextColor
from styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="https://web.reflex-assets.dev/other/logo.jpg", alt="Logo", width="100px",height="100px"),
#este se cambio desde el celular 2024 a 2023
        rx.text(
            f"TheObsidianBoy © 2023-{datetime.date.today().year}",
            font_size=Size.DEFAULT.value,
            margin_top=Size.SMALL.value
        ),
        padding_y=Size.BIG.value,
        padding_x=Size.BIG.value,
        direction="column",
        align="center",
        justify="center",
    )