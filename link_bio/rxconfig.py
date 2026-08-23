import reflex as rx

config = rx.Config(
    app_name="link_bio",
    cors_allowed_origins=[
        "https://link-bio-navy-ring.reflex.run",
        "http://localhost:3000",
        "http://localhost:8000"
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    api_url="https://theobsidianboy-web.up.railway.app"
)
