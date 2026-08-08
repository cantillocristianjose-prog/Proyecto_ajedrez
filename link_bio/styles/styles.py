import reflex as rx
from styles.colors import Color as Color
from styles.colors import TextColor as TextColor
from enum import Enum
#Constantes
MAX_WIDTH = "560px"

#Spacings
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"

class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    MEDIUM_SMALL = "2"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"

BASE_STYLE = {
    "background_color":Color.BACKGROUND.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color":TextColor.HEADER.value,
        "background_color":Color.PRIMARY.value,
        "_hover": {
            "background_color":Color.SECONDARY.value
        }
    }
}

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value
)

button_title_style = dict(
    font_size=Size.DEFAULT.value
)

button_body_style = dict(
    font_size=Size.MEDIUM.value
)
