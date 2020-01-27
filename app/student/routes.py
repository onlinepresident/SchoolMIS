from flask import Blueprint

blue = Blueprint('student', __name__, template_folder='templates', url_prefix='/student')

@blue.route('/')
def student():
    return 'Student Summary'

@blue.route('/profile')
def profile():
    return 'Student profile'
