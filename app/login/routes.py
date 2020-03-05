from flask import Blueprint, render_template, redirect, flash, url_for
from app.login.form import LoginForm
from flask_login import current_user,login_user
from app.main.models import User
from flask import request
from werkzeug.urls import url_parse

blue = Blueprint('login',__name__, template_folder = 'templates', url_prefix='/login')

@blue.route('/', methods = ['GET', 'POST'])
def index():
    return 'why'
    # if current_user.is_authenticated:
    #     return redirect(url_for('admin.index'))
    #
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #
    #     if user is None or not user.check_password(form.password.data):
    #         flash('login failed. Try again')
    #         return redirect(url_for('.index'))
    #
    #     login_user(user, remember = form.remember_me.data)
    #
    #     next_page = request.args.get('next')
    #
    #     if not next_page or url_parse(next_page).netloc != '':
    #         next_page = url_for('admin.index')
    #     return redirect(next_page)
    #
    #     return redirect(url_for('admin.index'))
    # return render_template('login/login.html', title = 'Sign In', form = form)
