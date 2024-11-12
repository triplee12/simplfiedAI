"""SimplifiedAI about us page"""

import reflex as rx

from simplifiedAI import ui


def about_us() -> rx.Component:
    # About Us Page
    return ui.base_layout(
        rx.vstack(
            rx.heading("Welcome to SimplifiedAI About Us!", size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )
