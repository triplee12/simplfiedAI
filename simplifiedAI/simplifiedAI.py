"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from . import pages, navigation


app = rx.App()
app.add_page(pages.index, route=navigation.routes.HOME_ROUTE)
app.add_page(pages.about_us, route=navigation.routes.ABOUT_US_ROUTE)
