"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def navbar(prop, *args, **kwargs) -> rx.Component:
    return rx.heading(prop, *args, **kwargs)


def base_layout(*args, **kwargs) -> rx.Component:
    return rx.container(
        navbar("Navbar"),
        *args, **kwargs
    )


def about_us() -> rx.Component:
    # About Us Page
    return base_layout(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to SimplifiedAI About Us!", size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return base_layout(
        rx.color_mode.button(position="top-right"),
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


app = rx.App()
app.add_page(index, route='/')
app.add_page(about_us, route='/about')
