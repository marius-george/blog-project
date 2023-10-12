import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

def create_app():
    

    # Import and register blueprints
    from blogproject.core.views import core
    from blogproject.users.views import users
    from blogproject.blog_posts.views import blog_posts
    from blogproject.custom_error.errors import custom_error

    app.register_blueprint(core)
    app.register_blueprint(users)
    app.register_blueprint(blog_posts)
    app.register_blueprint(custom_error)

    return app