import reflex as rx
import views.constants as constants
from styles.styles import Size,Spacing
from components.link_button import link_button
from components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Instragram",
                    "Sígueme en Instagram",
                    constants.INSTAGRAM_URL),
        link_button("Tiktok",
                    "Videos cortos y divertidos",
                    constants.TIKTOK_URL),
        link_button("Twitch",
                    "Directos los sabados y festivos",
                    constants.TWITCH_URL),
        link_button("Youtube",
                    "Videos largo en duracion ¡con el doble de diversion!",
                    constants.YOUTUBE_URL),
        width="100%",
        spacing=Spacing.MEDIUM_BIG.value,
    )