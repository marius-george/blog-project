# errors page
from flask import Blueprint, render_template

custom_error = Blueprint('custom_error', __name__)


@custom_error.app_errorhandler(404)
def custom_error_404(error):
    return render_template('custom_error/404.html'), 404


@custom_error.app_errorhandler(403)
def custom_error_403(error):
    return render_template('custom_error/403.html'), 403
