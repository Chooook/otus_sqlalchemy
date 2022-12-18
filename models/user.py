from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    false,
    func,
)

from base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer,
                primary_key=True)
    username = Column(String(32),
                      unique=True,
                      nullable=False)
    archived = Column(Boolean,
                      default=False,
                      server_default=false())
    created_at = Column(DateTime,
                        default=datetime.utcnow,
                        server_default=func.now())

    def __str__(self):
        return (f"User(id={self.id}, username={self.username!r}, "
                f"archived={self.archived}, created_at={self.created_at!r})")

    def __repr__(self):
        return self.__str__()
