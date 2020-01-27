from flask import Blueprint, render_template, redirect, flash
from app.login.form import LoginForm

blue = Blueprint('login',__name__, template_folder = 'templates', url_prefix='/login')

@blue.route('/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # flash('Login requested for user {}, remember me {}'.format(form.username.data,form.remember_me.data))
        return redirect('/')
    return render_template('login/login.html', title = 'Sign In', form = form)
