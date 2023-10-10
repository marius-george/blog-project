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
    # basedir = os.path.abspath(os.path.dirname(__file__))
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    #     os.path.join(basedir, 'data.sqlite')
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    # app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
    # app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

    if os.environ.get("DEVELOPMENT") == "True":
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
    else:
        uri = os.environ.get("DATABASE_URL")
        print("uri", uri)
        if uri.startswith("postgres://"):
            uri = uri.replace("postgres://", "postgresql://", 1)
        app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku

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