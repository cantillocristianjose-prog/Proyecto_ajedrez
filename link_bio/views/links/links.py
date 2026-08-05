import reflex as rx
from components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Instragram","https://www.instagram.com/theobsidianboy?igsh=ejlmZ3EyNTI2c3R2"),
        link_button("Tiktok","https://www.tiktok.com/@theobsidianboy?_t=ZS-8wpNOgZA0nK&_r=1"),
        link_button("Twitch","https://www.twitch.tv/theobsidianboy"),
        link_button("Youtube","https://www.youtube.com/@TheObsidianBoy"),
    )