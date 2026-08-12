import reflex as rx

config = rx.Config(
    app_name="link_bio",
    favicon_url="/foto_de_sebas.ico",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
