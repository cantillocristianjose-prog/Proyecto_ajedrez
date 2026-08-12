import reflex as rx
import datetime
import styles.styles as styles
from styles.colors import TextColor as TextColor
from styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="icons/foto_de_sebas.jpeg",
            alt="Logo de TheObsidanBoy",
            width=Size.VERY_BIG.value,
            height=Size.VERY_BIG.value
        ),
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