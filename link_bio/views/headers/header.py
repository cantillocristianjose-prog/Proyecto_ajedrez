import reflex as rx
from components.link_icon import link_icon
from components.info_text import info_text
from styles.styles import Size,Spacing

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="TB", size="6"),
            rx.vstack(
                rx.heading("TheObsidianBoy", size="7"),
                rx.text("@TheObsidianBoy"),
                rx.hstack(
                    link_icon("https://www.instagram.com/theobsidianboy?igsh=ejlmZ3EyNTI2c3R2"),
                    link_icon("https://www.instagram.com/theobsidianboy?igsh=ejlmZ3EyNTI2c3R2"),
                    link_icon("https://www.instagram.com/theobsidianboy?igsh=ejlmZ3EyNTI2c3R2"),
                ),
                align="start",
            ),
        ),
        rx.flex(
            info_text("16", " años de edad"),
            rx.spacer(),
            info_text("16", " años a cumplir el canal"),
            rx.spacer(),
            info_text("5", " años el canal segundario a cumplir"),
            width="100%",
        ),
        rx.text("""Bienvenido a mi canal! soy TheObsidianBoy, 
        un Youtuber Colombiano🇨🇴 , 
        amante a los videojuegos como Minecraft, 
        Resident Evil, 
        Devil May Cry y Halo, 
        espero que la pases bien por aquí con gameplays que disfrutes! ♡ """),
        spacing=Spacing.BIG.value,
        align="start",
    )