import reflex as rx

config = rx.Config(
    app_name="link_bio",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://link-bio-gold-orca.reflex.run"
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    api_url="https://apithe.up.railway.app"
)
