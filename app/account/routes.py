from flask import Blueprint

blue = Blueprint('account', __name__, template_folder='templates', url_prefix='/account')

@blue.route('')
def accounts():
    return 'accounts information'

@blue.route('/payment')
def payment():
    return 'payment information'


@blue.route('receipt')
def receipt():
    return 'receipt information'
