import reflex as rx
import views.constants as const
from routers import Route
from styles.styles import Size,Spacing
from components.link_button import link_button
from components.title import title

def libros_link() -> rx.Component:
    return rx.vstack(
        title("Libros"),
        link_button("EFECTO FRAGMENTO",
                    "Etiquetas: ficcíon, suspenso, vieajes en el tiempo",
                    "/icons/libro.svg",
                    const.EFECTO_FRAGMENTO),
        link_button("EFECTO FRAGMENTO II",
                    "Etiquetas: ficcíon, fragmento, suspenso, viajes en el tiempo",
                    "/icons/libro.svg",
                    const.EFECTO_FRAGMENTO2),
        link_button("EFECTO FRAGMENTO: Umbral De La Mente Partida",
                    "Etiquetas: suspenso, terror, terror psicologico",
                    "/icons/libro.svg",
                    const.EFECTO_UMBRAL),
        width="100%"
    )