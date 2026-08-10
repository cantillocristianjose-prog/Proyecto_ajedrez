import reflex as rx
import views.constants as const
from styles.fonts import Font
from components.title import title
from styles.colors import TextColor
from styles.colors import Color
from components.link_icon import link_icon
from components.info_text import info_text
from styles.styles import Size,Spacing

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="TB",size="6",bg=Color.PRIMARY.value,color=Color.SECONDARY.value),
            rx.vstack(
                rx.heading(
                    "TheObsidianBoy",
                    size="7"
                ),
                rx.text("@TheObsidianBoy", margin_top=Size.ZERO.value,color=TextColor.BODY.value),
                rx.hstack(
                    link_icon(const.TIKTOK_URL),
                    link_icon(const.INSTAGRAM_URL),
                    link_icon(const.YOUTUBE_URL),
                ),
                align="start",
                spacing=Spacing.ZERO.value
            ),
            spacing=Spacing.MEDIUM_SMALL.value
        ),
        rx.flex(
            info_text("16", " años de edad"),
            rx.spacer(),
            info_text("16", " años a cumplir el canal"),
            rx.spacer(),
            info_text("5", " años el canal segundario a cumplir"),
            width="100%",
            spacing="5",
        ),
        rx.text(
            """Bienvenido a mi canal! soy TheObsidianBoy, 
            un Youtuber Colombiano🇨🇴 , 
            amante a los videojuegos como Minecraft, 
            Resident Evil, 
            Devil May Cry y Halo, 
            espero que la pases bien por aquí con gameplays que disfrutes! ♡ """,
            color=TextColor.BODY.value
        ),
        spacing=Spacing.BIG.value,
        align="start",
    )