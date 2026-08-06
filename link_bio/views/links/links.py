import reflex as rx
from components.link_button import link_button
from components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Instragram",
                    "Sígueme en Instagram",
                    "https://www.instagram.com/theobsidianboy?igsh=ejlmZ3EyNTI2c3R2"),
        link_button("Tiktok",
                    "Videos cortos y divertidos",
                    "https://www.tiktok.com/@theobsidianboy?_t=ZS-8wpNOgZA0nK&_r=1"),
        link_button("Twitch",
                    "Directos los sabados y festivos",
                    "https://www.twitch.tv/theobsidianboy"),
        link_button("Youtube",
                    "Videos largo en duracion ¡con el doble de diversion!",
                    "https://www.youtube.com/@TheObsidianBoy"),
        width="100%",
    )