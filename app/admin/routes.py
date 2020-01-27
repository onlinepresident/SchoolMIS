from flask import Blueprint
from flask import render_template

blue = Blueprint('admin', __name__, template_folder='templates', url_prefix='/admin')

@blue.route('/')
def admin():
    return 'Admin dashboard'
