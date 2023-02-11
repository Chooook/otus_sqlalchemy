from flask import Blueprint, render_template, request

from models import User

users_app = Blueprint('users', __name__)


@users_app.get('/create_user')
def create_user():
    # username = request.args.get('username')
    # User.create_user(username)
    return render_template('users/create_user.html')


@users_app.get('/')
def get_all_users():
    users = User.query.all()
    return render_template('/', users=users)


@users_app.get('/<int:user_id>')
def get_user_by_id(user_id: int):
    return {
        'user': {'id': user_id}
    }


@users_app.get('/user_name')
def get_user_by_name(user_name: str):
    return {
        'user': {'name': user_name}
    }
