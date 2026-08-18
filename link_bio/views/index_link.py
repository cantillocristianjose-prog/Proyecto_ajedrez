import reflex as rx
import views.constants as constants
from routers import Route
from styles.styles import Size,Spacing
from components.link_button import link_button
from components.title import title

def index_link() -> rx.Component:
    return rx.vstack(
        title("Redes sociales"),
        link_button("Instragram",
                    "Sígueme en Instagram",
                    "icons/instagram.svg",
                    constants.INSTAGRAM_URL),
        link_button("Tiktok",
                    "Videos cortos y divertidos",
                    "icons/tiktok.svg",
                    constants.TIKTOK_URL),
        link_button("Twitch",
                    "Directos los sabados y festivos",
                    "icons/twitch-brands-solid-full.svg",
                    constants.TWITCH_URL),
        title("Canales"),
        link_button("Youtube",
                    "Videos para pasar el rato",
                    "icons/youtube.svg",
                    constants.YOUTUBE_URL),
        link_button("Youtube secundario",
                    "Proyecto en youtube",
                    "icons/youtube.svg",
                    constants.YOUTUBE_SECONDARY_URL),
        link_button(
            "Nuevo comienzo",
            "¿y que tal si empezamos de nuevo?",
            "icons/youtube.svg",
            Route.VIDEOS.value,
            is_external=False
        ),
        width="100%"
    )