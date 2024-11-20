# import asyncio
from typing import List
import reflex as rx
import sqlmodel
from simplifiedAI.models import ChatModel, ChatMessageModel
from . import ai


class ChatMessage(rx.Base):

    message: str
    is_bot: bool = False


class ChatState(rx.State):
    chat_model: ChatModel = None
    did_submit: bool = False
    not_found: bool = False
    messages: List[ChatMessage] = []
    
    @rx.var
    def user_did_submit(self) -> bool:
        return self.did_submit

    def get_session_id(self) -> int:
        try:
            my_session_id = int(self.router.page.params.get('chat_id'))
        except:
            my_session_id = 0
        return my_session_id

    def create_new_chat_sessions(self):
        with rx.session() as db_session:
            obj = ChatModel()
            db_session.add(obj)
            db_session.commit()
            db_session.refresh(obj)
            self.chat_model = obj

    def clear_and_start_new_chat(self):
        self.chat_model = None
        self.create_new_chat_sessions()
        self.messages = []
        yield

    def get_chat_sessions_from_db(self, session_id=None):
        if session_id is None:
            session_id = self.get_session_id()
        with rx.session() as db_session:
            sql_statement = sqlmodel.select(
                ChatModel
            ).where(ChatModel.id == session_id)
            result = db_session.exec(sql_statement).one_or_none()
            if result is None:
                self.not_found = True
            self.chat_model = result
            messages = result.messages
            for message in messages:
                msg_content = message.content
                msg_role = False if message.role == "user" else True
                self.append_message_to_ui(msg_content, msg_role)

    def on_detail_load(self):
        session_id = self.get_session_id()
        if isinstance(session_id, int):
            self.get_chat_sessions_from_db(session_id=session_id)

    def on_load(self):
        if self.chat_model is None:
            self.create_new_chat_sessions()

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
