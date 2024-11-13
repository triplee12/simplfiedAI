import reflex as rx
from decouple import config

DATABASE_URL = config("DATABASE_URL", cast=str)

config = rx.Config(
    app_name="simplifiedAI",
    db_url=DATABASE_URL,
)