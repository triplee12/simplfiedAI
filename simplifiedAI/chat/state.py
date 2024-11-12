import reflex as rx



class ChatState(rx.State):
    did_submit: bool = False

    def handle_submit(self, form_data: dict):
        print(form_data)
