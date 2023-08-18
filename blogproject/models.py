from blogproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    """
    Load a user object from the database using the user ID.

    Parameters:
        user_id (str): The ID of the user to load.

    Returns:
        User: The User object representing the loaded user.
    """
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    """
    Class representing a user of the application.

    Attributes:
        id (int): The unique identifier for the user.
        profile_image (str): The filename of the user's profile image.
        email (str): The email address of the user.
        username (str): The unique username of the user.
        password_hash (str): The hashed password of the user.
        posts (list of BlogPost): List of blog posts authored by the user.
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(
        db.String(64), nullable=False, default='snake.png')
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    posts = db.relationship('BlogPost', backref='author', lazy=True)

    def __init__(self, email, username, password):
        """
        Initialize a User object.

        Parameters:
            email (str): The email address of the user.
            username (str): The username of the user.
            password (str): The plain-text password of the user.

        Returns:
            None
        """
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Check if the provided password matches the user's hashed password.

        Parameters:
            password (str): The plain-text password to check.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username {self.username}"


class BlogPost(db.Model):
    """
    Class representing a blog post.

    Attributes:
        id (int): The unique identifier for the blog post.
        user_id (int): The ID of the user who authored the blog post.
        date (datetime): The date and time when the blog post was created.
        title (str): The title of the blog post.
        text (str): The content of the blog post.
    """

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(160), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text, user_id):
        """
        Initialize a BlogPost object.

        Parameters:
            title (str): The title of the blog post.
            text (str): The content of the blog post.
            user_id (int): The ID of the user who authored the blog post.

        Returns:
            None
        """
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- {self.title}"
