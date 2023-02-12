from http import HTTPStatus

from flask import Blueprint, render_template, request, url_for, redirect, flash

from models import User
from views.forms import UserForm

users_app = Blueprint('users', __name__)


@users_app.route('/create', methods=['GET', 'POST'], endpoint='create')
def create_user():
    form = UserForm()
    if request.method == 'GET':
        return render_template('users/create.html', form=form)
    if not form.validate_on_submit():
        return (
            render_template('users/create.html', form=form),
            HTTPStatus.BAD_REQUEST
        )
    username = form.username.data
    user = User.create_user(username=username)
    flash(f"User {user.username} created")
    url = url_for('users.list')
    return redirect(url)


@users_app.get('/', endpoint='list')
def users_list():
    users = User.query.all()
    return render_template('users/list.html', users=users)


@users_app.get('/<int:user_id>', endpoint='details')
def user_details(user_id: int):
    user = User.query.get_or_404(
        user_id,
        description=f'User with id: {user_id} not found'
    )
    return render_template('users/details.html', user=user)


@users_app.get('/user_name')
def get_user_by_name(user_name: str):
    return {
        'user': {'name': user_name}
    }
