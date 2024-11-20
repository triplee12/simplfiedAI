from turtle import width
import reflex as rx

from simplifiedAI import ui
from .state import ChatMessage, ChatState
from .form import chat_form


message_style = dict(
    display='inline-block',
    padding='1em',
    border_radius="8px",
    max_width=["30em", "30em", "50em", "50em", "50em", "50em"]
)


def message_box(chat_message: ChatMessage) -> rx.Component:
    return rx.box(
        rx.box(
            rx.markdown(
                chat_message.message,
                background_color=rx.cond(
                    chat_message.is_bot, rx.color('mauve', 4), rx.color('blue', 4)
                ),
                color=rx.cond(
                    chat_message.is_bot, rx.color('mauve', 12), rx.color('blue', 12)
                ),
                **message_style,
            ),
            text_align=rx.cond(chat_message.is_bot, 'left', 'right'),
            margin_top='1em',
        ),
        width="100%",
    )


def chat_page():
    return ui.base_layout(
        rx.vstack(
            rx.hstack(
                rx.heading("Chat here!", size="5"),
                rx.button("+ New chat", on_click=ChatState.clear_and_start_new_chat),
            ),
            rx.box(
                rx.foreach(ChatState.messages, message_box),
                width="100%",
            ),
            chat_form(),
            margin="3rem auto",
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )
