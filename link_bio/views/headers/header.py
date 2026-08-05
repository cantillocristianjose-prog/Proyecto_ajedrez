import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="TB", size="5"),
        rx.text("@TheObsidianBoy"),
        rx.text("Hola mi nombre es TheObsidianBOy"),
        rx.text("""Bienvenido a mi canal! soy TheObsidianBoy, 
        un Youtuber Colombiano🇨🇴 , 
        amante a los videojuegos como Minecraft, 
        Resident Evil, 
        Devil May Cry y Halo, 
        espero que la pases bien por aquí con gameplays que disfrutes! ♡ """),
        width="100%",
        border_radius="0.5rem",
        direction="column",
        align="center",
        justify="center",
    )