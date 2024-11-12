"""SimplifiedAI home page"""

from rxconfig import config

from simplifiedAI import ui
import reflex as rx


def index() -> rx.Component:
    # Welcome Page (Index)
    return ui.base_layout(
        rx.vstack(
            rx.heading("Welcome to SimplifiedAI!", size="9"),
            rx.text(
                "Get started by editing something! ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )
