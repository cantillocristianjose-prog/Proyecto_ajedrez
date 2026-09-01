import reflex as rx
from datetime import datetime,timezone,timedelta
#Comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview = "https://www.infobae.com/america/perrosygatos/2022/01/03/8-datos-curiosos-que-desconocemos-de-los-gatos/"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview}
]



#Index

index_title = "El cuartel de TheObsidianBoy"
index_descripcion = "Hola mi nombre es TheObsidianBoy y soy creador de contenido"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_descripcion}
]

index_meta.extend(_meta)
#Videos

libros_title = "TheObsidianBoy | Libros"
libros_descripcion = "este es un listado de mis libros"

videos_meta = [
    {"name": "og:title", "content": libros_title},
    {"name": "og:description", "content": libros_descripcion}
]
videos_meta.extend(_meta)

#Date

def next_date(dates: dict) -> str:

    if len(dates) == 0:
        return ""

    now = datetime.now()
    current_weekday = now.weekday()
    current_time = now.astimezone().timetz()

    for index in range(7):

        day = str((current_weekday + index) % 7)

        if day not in dates or dates[day] == "":
            continue

        time_utc = datetime.strptime(dates[day], "%H:%M").time().replace(tzinfo=timezone.utc)

        time = datetime.combine(now.date(),time_utc).astimezone().timetz()

        if current_time < time or index > 0:
            next_date = now + timedelta(days=index)

            formatted_next_date = next_date.strftime(
                "Hoy, %d/%m") if index == 0 else next_date.strftime("%A, %d/%m")

            formatted_next_time = time_utc.strftime("%H:%M")

            return f"{day} - {formatted_next_date} a las {formatted_next_time}"

    return ""