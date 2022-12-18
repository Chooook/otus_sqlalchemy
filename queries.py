from base import Base, Session
from models import User
# Как обойти "неиспользуемый импорт"??
# Без него не создается таблица
# Кроме решения с переносом Base в файл user
# Тот же прикол, что и с фикстурами pytest


def main():
    Base.metadata.drop_all()
    Base.metadata.create_all()

    session = Session()

    # create_user(session, "john")
    # create_user(session, "sam")

    # create_users(session, "Ленин", "Сталин", "Гитлер", "Ницше")
    # get_all_users(session)
    # get_user_by_username(session, "bob")
    # get_user_by_username(session, "jack")
    # get_user_by_id(session, 1)
    # get_user_by_id(session, 100)

    # get_users_by_username_match(session, "a")
    # get_users_by_username_match(session, "j")
    # get_users_by_username_match(session, "x")

    session.close()


# def create_user(session: SessionType, username: str) -> User:
#     user = User(username=username)
#     session.add(user)
#     session.commit()
#     return user
#
#
# def create_users(session: SessionType, *usernames: str) -> list[User]:
#     users = []
#     for username in usernames:
#         user = User(username=username)
#         session.add(user)
#         users.append(user)
#
#     session.commit()
#
#     return users
#
#
# def get_all_users(session: SessionType) -> list[User]:
#     users = session.query(User).order_by(User.id).all()
#     print("users:", users)
#     return users
#
#
# def get_user_by_username(session: SessionType, username: str) -> User | None:
#     # user = session.query(User).filter_by(username=username).first()
#     # user = session.query(User).filter_by(username=username).one()
#     user = session.query(User).filter_by(username=username).one_or_none()
#     print("user:", user)
#     return user
#
#
# def get_user_by_id(session: SessionType, user_id: int) -> User | None:
#     user = session.get(User, user_id)
#     print("user:", user)
#     return user
#
#
# def get_users_by_username_match(session: SessionType, username_part: str) \
# -> list[User]:
#     users = session.query(User).filter(
#         User.username.ilike(f"%{username_part}%")).all()
#     print("user:", users)
#     return users


if __name__ == '__main__':
    main()
