import reflex as rx
import datetime
import views.constants as const
from styles.fonts import Font
from components.title import title
from styles.colors import TextColor
from styles.colors import Color
from components.link_icon import link_icon
from components.link_button import link_button
from components.info_text import info_text
from styles.styles import Size,Spacing
from model.Live import Live
from state.PageState import PageState
años_actual = datetime.date.today().year

def header(details = True, live_status: Live = Live(live=False,title= ""), next_live= "") -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback="TB",
                size="6",
                bg=Color.PRIMARY.value,
                color=Color.CONTENT.value,
                src="/icons/foto_de_sebas.jpeg",
                radius="full",
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.cond(
                live_status.live,
                rx.link(
                    rx.badge(
                        rx.image(src="/icons/twitch-brands-solid-full.svg",width="20px",height="20px"),
                        radius="full",
                        size="2",
                        color_scheme="purple",
                        class_name="blink"
                    ),
                    href=const.TWITCH_URL,
                    is_external=True
                )
            ),    
            rx.vstack(
                rx.heading(
                    "TheObsidianBoy",
                    size="7"
                ),
                rx.text("@TheObsidianBoy", margin_top=Size.ZERO.value,color=TextColor.BODY.value),
                rx.hstack(
                    link_icon(
                        "icons/tiktok.svg",
                        const.TIKTOK_URL,
                        "tiktok"
                    ),
                    link_icon(
                        "icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "instagram"
                    ),
                    link_icon(
                        "icons/youtube.svg",
                        const.YOUTUBE_URL,
                        "youtube"
                    ),
                    link_icon(
                        "icons/github.svg",
                        const.REPOSITORIO_MIO,
                        "Repositorio del proyecto"
                    ),
                    spacing=Spacing.DEFAULT.value
                ),
                align="start",
                spacing=Spacing.ZERO.value
            ),
            spacing=Spacing.MEDIUM_SMALL.value
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text("16", " años de edad"),
                    rx.spacer(),
                    info_text(f"{datetime.date.today().year - 2023}", " años a cumplir el canal"),
                    width="100%"
                ),
                rx.cond(
                    live_status.live,
                    link_button(
                        "En vivo",
                        live_status.title,
                        "/icons/twitch-brands-solid-full.svg",
                        const.TWITCH_URL,
                        animated=True
                    ),
                    rx.cond(
                        next_live,
                        link_button(
                            "Proximo directo",
                            next_live,
                            "/icons/twitch-brands-solid-full.svg",
                            const.TWITCH_URL,
                            animated=True
                        ),
                    ),
                ),
                rx.text(
                        """Bienvenido a mi canal! soy TheObsidianBoy, 
                    un Youtuber Colombiano🇨🇴 , 
                    amante a los videojuegos como Minecraft, 
                    Resident Evil, 
                    Devil May Cry y Halo, 
                    espero que la pases bien por aquí con gameplays que disfrutes! ♡ """,
                    color=TextColor.BODY.value,
                    font_size=Size.MEDIUM.value
                ),
                width="100%",
                spacing=Spacing.BIG.value
            )
        ),
        spacing=Spacing.BIG.value,
        align="start",
    )