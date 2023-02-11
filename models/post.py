from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    Column, Integer, String, DateTime, func, ForeignKey, Text
)

from .db import db

if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class Post(db.Model):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    # user_id = Column(
    #     Integer,
    #     ForeignKey('users.id', ondelete='CASCADE'),
    #     nullable=False
    # )
    title = Column(String, unique=True, nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime,
                        default=datetime.utcnow,
                        server_default=func.now())

    def __str__(self):
        return (f"Post(id={self.id}, title={self.title},"
                f" text={self.text}, created_at={self.created_at!r})")

    def __repr__(self):
        return self.__str__()

    @classmethod
    def create_post(cls, session, title: str, text: str):
        post = Post(title=title, text=text)
        session.add(post)
        session.commit()
        return post

    if TYPE_CHECKING:
        query: Query
