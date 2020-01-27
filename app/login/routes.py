from flask import Blueprint, render_template, redirect, flash, url_for
from app.login.form import LoginForm
from flask_login import current_user,login_user
from app.main.models import User

blue = Blueprint('login',__name__, template_folder = 'templates', url_prefix='/login')

@blue.route('/', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.admin'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('login failed. Try again')
            return redirect(url_for('login.login'))

        login_user(user, remember = form.remember_me.data)
        return redirect(url_for('admin.admin'))
    return render_template('login/login.html', title = 'Sign In', form = form)
