# blogproject __init__.py
from flask import Flask

app = Flask(__name__)


from blogproject.core.views import core
app.register_blueprint(core)
