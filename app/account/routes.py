from flask import Blueprint
from flask_login import login_required
blue = Blueprint('account', __name__, template_folder='templates', url_prefix='/account')

@blue.route('/')
@login_required
def accounts():
    return 'accounts information'

@blue.route('/payment')
def payment():
    return 'payment information'


@blue.route('/receipt')
def receipt():
    return 'receipt information'
