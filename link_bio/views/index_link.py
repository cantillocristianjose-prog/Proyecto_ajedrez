import reflex as rx
import views.constants as constants
import styles.styles as styles
from routers import Route
from styles.styles import Size,Spacing
from components.link_button import link_button
from components.title import title
from components.featured_link import featured_link
from model.Featured import Featured
from state.PageState import PageState

def index_link(featured: list[Featured]) -> rx.Component:
    return rx.vstack(
        title("Redes sociales"),
        link_button("Instragram",
                    "Sígueme en Instagram",
                    "/icons/instagram.svg",
                    constants.INSTAGRAM_URL),
        link_button("Tiktok",
                    "Videos cortos y divertidos",
                    "/icons/tiktok.svg",
                    constants.TIKTOK_URL),
        link_button("Twitch",
                    "Directos los sabados y festivos",
                    "/icons/twitch-brands-solid-full.svg",
                    constants.TWITCH_URL),

        rx.cond(
            featured,
            rx.vstack(
                title("Destacada"),
                rx.grid(
                    rx.foreach(
                        featured,
                        featured_link
                    ),
                    columns={"initial": "1", "sm": "2"},
                    spacing=Spacing.DEFAULT.value,
                    class_name=styles.FADEIN_ANIMATION
                )
            )
        ),
        title("Canales"),
        link_button("Youtube",
                    "Videos para pasar el rato",
                    "/icons/youtube.svg",
                    constants.YOUTUBE_URL),
        link_button("Youtube secundario",
                    "Proyecto en youtube",
                    "/icons/youtube.svg",
                    constants.YOUTUBE_SECONDARY_URL),
        link_button(
            "Más sobre mi",
            "Apartado de contenido derivado o diferente de lo habitual",
            "/icons/star.svg",
            Route.LIBROS.value,
            is_external=False
        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,
    )