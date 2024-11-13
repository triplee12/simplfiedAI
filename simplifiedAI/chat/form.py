import reflex as rx

from .state import ChatState


def chat_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.text_area(
                name='message',
                placeholder='Type your message here',
                width='100%',
                required=True
            ),
            rx.hstack(
                rx.button('Submit', type='submit'),
                rx.cond(
                    ChatState.user_did_submit,
                    rx.text('Loading...'),
                    rx.fragment(),
                ),
            ),
        ),
        on_submit=ChatState.handle_submit,
        reset_on_submit=True
    )
