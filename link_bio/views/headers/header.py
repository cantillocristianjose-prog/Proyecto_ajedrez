import reflex as rx
from components.link_icon import link_icon
from components.info_text import info_text
from styles.styles import Size,Spacing
def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="TB", size="6"),
            rx.vstack(rx.heading("TheObsidianBoy",size="7"),
                      rx.text("@TheObsidianBoy"),),
            maring_y=Spacing.VERY_BIG.value
        ),
        rx.hstack(
            link_icon("https://www.instagram.com/theobsidianboy?igsh=ejlmZ3EyNTI2c3R2"),
            link_icon("https://www.instagram.com/theobsidianboy?igsh=ejlmZ3EyNTI2c3R2"),
            link_icon("https://www.instagram.com/theobsidianboy?igsh=ejlmZ3EyNTI2c3R2")
        ),
        rx.flex(
            info_text("16","años de edad")
        ),
        rx.text("""Bienvenido a mi canal! soy TheObsidianBoy, 
        un Youtuber Colombiano🇨🇴 , 
        amante a los videojuegos como Minecraft, 
        Resident Evil, 
        Devil May Cry y Halo, 
        espero que la pases bien por aquí con gameplays que disfrutes! ♡ """),
        width="100%",
        spacing= Spacing.BIG.value,
        border_radius="0.5rem",
        direction="column",
        align="start",
        justify="center",
    )