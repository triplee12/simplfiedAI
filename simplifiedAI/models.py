from datetime import datetime, timezone
from typing import List
from sqlmodel import Field, Relationship
import reflex as rx
import sqlalchemy


def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)


class ChatModel(rx.Model, table=True):
    messages: List['ChatMessageModel'] = Relationship(back_populates='chat')
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    )
    updated_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'onupdate': sqlalchemy.func.now(),
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    )


class ChatMessageModel(rx.Model, table=True):
    chat_id: int = Field(default=None, foreign_key='chatmodel.id')
    chat: ChatModel = Relationship(back_populates="messages")
    content: str
    role: str
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    )
