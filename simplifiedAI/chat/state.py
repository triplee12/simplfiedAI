# import asyncio
from typing import List
import reflex as rx
from simplifiedAI.models import ChatModel, ChatMessageModel
from . import ai


class ChatMessage(rx.Base):

    message: str
    is_bot: bool = False


class ChatState(rx.State):
    chat_model: ChatModel = None
    did_submit: bool = False
    messages: List[ChatMessage] = []
    
    @rx.var
    def user_did_submit(self) -> bool:
        return self.did_submit
    
    def on_load(self):
        print("Running on load")
        if self.chat_model is None:
            with rx.session() as db_session:
                obj = ChatModel()
                db_session.add(obj)
                db_session.commit()
                db_session.refresh(obj)
                self.chat_model = obj
    
    def insert_message_to_db(self, content, role="unknown"):
        if self.chat_model is None:
            return
        if not isinstance(self.chat_model, ChatModel):
            return
        with rx.session() as db_session:
            data = {
                "chat_id": self.chat_model.id,
                "content": content,
                "role": role
            }
            obj = ChatMessageModel(**data)
            db_session.add(obj)
            db_session.commit()

    def append_message_to_ui(self, message, is_bot: bool = False):
        self.messages.append(ChatMessage(message=message, is_bot=is_bot))

    def get_gpt_messages(self):
        gpt_messages = [
            {
                "role": "system",
                "content": "Brainstorm"
            }
        ]
        for chat_message in self.messages:
            role = 'user'
            if chat_message.is_bot:
                role = 'system'
            gpt_messages.append(
                {
                    "role": role,
                    "content": chat_message.message
                }
            )
        return gpt_messages

    async def handle_submit(self, form_data: dict):
        user_message = form_data.get('message')
        if user_message:
            self.did_submit = True
            self.append_message_to_ui(message=user_message, is_bot=False)
            self.insert_message_to_db(content=user_message, role="user")
            yield
            gpt_messages = self.get_gpt_messages()
            bot_response = ai.get_llm_response(gpt_messages)
            # await asyncio.sleep(2)
            self.did_submit = False
            self.append_message_to_ui(message=bot_response, is_bot=True)
            self.insert_message_to_db(content=bot_response, role="system")
            yield
