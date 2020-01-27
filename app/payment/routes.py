from flask import Blueprint

blue= Blueprint('payment', __name__,template_folder='templates', url_prefix='/payment')

@blue.route('/')
def payment():
    return 'payment details'
