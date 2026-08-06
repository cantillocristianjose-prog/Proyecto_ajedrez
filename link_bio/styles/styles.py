import reflex as rx

#Constantes
MAX_WIDTH = "600PX"

#Sizes
SMALL_SIZE_Space = "0.5em"
SMEDIUM_SIZE_Space = "0.8em"
MEDIUM_SIZE_Space = "1em"
BIG_SIZE_Space = "2em"

BASE_STYLE = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": SMALL_SIZE_Space,
        "border_radius": MEDIUM_SIZE_Space
    }
}

title_style = dict(
    width="100%",
    padding_top=MEDIUM_SIZE_Space
)

button_title_style = dict(
    font_size = MEDIUM_SIZE_Space
)

button_body_style = dict(
    font_size = SMEDIUM_SIZE_Space
)
