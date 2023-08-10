import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secretblog'

    # Database setup #
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Login configs
    login_manager.init_app(app)
    login_manager.login_view = 'users.login'

    from blogproject.core.views import core
    from blogproject.users.views import users
    from blogproject.blog_posts.views import blog_posts
    from blogproject.custom_error.errors import custom_error

    app.register_blueprint(core)
    app.register_blueprint(users)
    app.register_blueprint(blog_posts)
    app.register_blueprint(custom_error)

    return app
