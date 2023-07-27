# blogproject __init__.py
from flask import Flask

app = Flask(__name__)


from blogproject.core.views import core
from blogproject.custom_error.errors import custom_error
app.register_blueprint(core)
app.register_blueprint(custom_error)
