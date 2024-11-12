"""SimplifiedAI navigation bar component."""

import reflex as rx

from simplifiedAI import navigation


def navbar_icons_item(
    text: str, icon: str, url: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", weight="medium"),
        ),
        href=url,
    )


def navbar_icons_menu_item(
    text: str, icon: str, url: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16),
            rx.text(text, size="3", weight="medium"),
        ),
        href=url,
    )


def base_navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "SimplifiedAI", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_icons_item("Home", "home", navigation.routes.HOME_ROUTE),
                    navbar_icons_item(
                        "Services", "layers", "/#"
                    ),
                    navbar_icons_item(
                        "About Us", "album", navigation.routes.ABOUT_US_ROUTE
                    ),
                    navbar_icons_item(
                        "Contact", "mail", "/#"
                    ),
                    navbar_icons_item(
                        "Chat", "album", navigation.routes.CHAT_ROUTE
                    ),
                    spacing="6",
                ),
                rx.color_mode.button(position="top-right"),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "SimplifiedAI", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        navbar_icons_menu_item(
                            "Home", "home", navigation.routes.HOME_ROUTE
                        ),
                        navbar_icons_menu_item(
                            "Services", "layers", "/#"
                        ),
                        navbar_icons_menu_item(
                            "About Us", "album", navigation.routes.ABOUT_US_ROUTE
                        ),
                        navbar_icons_menu_item(
                            "Contact", "mail", "/#"
                        ),
                        navbar_icons_menu_item(
                            "Chat", "album", navigation.routes.CHAT_ROUTE
                        ),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )
