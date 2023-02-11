from flask import Flask, request, render_template
from flask_migrate import Migrate
# from werkzeug.exceptions import NotFound

from models import db
from views import users_app

app = Flask(__name__)

DB_URI = 'postgresql+pg8000://chook:passwd@localhost:5432/blog'
app.config.update(
    SQLALCHEMY_DATABASE_URI=DB_URI,
    SQLALCHEMY_ECHO=True,
)

app.register_blueprint(users_app, url_prefix='/users')

db.init_app(app)
migrate = Migrate(app, db)


# @app.cli.command('db-create-all')
# def db_create_all():
#     db.create_all()
#
#
# @app.cli.command('db-drop-all')
# def db_drop_all():
#     db.drop_all()


@app.route('/')
def root_view():
    return render_template('index.html')


@app.route('/args')
def get_args():
    return request.args.to_dict(flat=False)


@app.route('/hello')
def greeting():
    name = request.args.get("name")
    return f'Hello {name}!'
    # return f'Hello {request.args.getlist("name")}'


if __name__ == '__main__':
    app.run(debug=True)
