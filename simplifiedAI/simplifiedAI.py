"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from . import chat, pages, navigation


app = rx.App()
app.add_page(pages.index, route=navigation.routes.HOME_ROUTE)
app.add_page(pages.about_us, route=navigation.routes.ABOUT_US_ROUTE)
app.add_page(
    chat.chat_page,
    route=navigation.routes.CHAT_ROUTE,
    on_load=chat.state.ChatState.on_load
)
