from flask import Blueprint
from flask_login import login_required
blue = Blueprint('student', __name__, template_folder='templates', url_prefix='/student')

@blue.route('/')
@login_required
def student():
    return 'Student Summary'

@blue.route('/profile')
def profile():
    return 'Student profile'
