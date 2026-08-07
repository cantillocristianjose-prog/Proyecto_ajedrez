import reflex as rx
from enum import Enum
#Constantes
MAX_WIDTH = "600PX"

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
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Spacing.BIG.value,
        "border_radius": Spacing.MEDIUM_BIG.value
    }
}

title_style = dict(
    width="100%",
    padding_top=Spacing.MEDIUM_BIG.value
)

button_title_style = dict(
    font_Spacing = Spacing.MEDIUM_BIG.value
)

button_body_style = dict(
    font_Spacing = Spacing.MEDIUM_BIG.value
)
