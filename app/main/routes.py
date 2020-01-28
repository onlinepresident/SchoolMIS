
from app import app
from flask import render_template, redirect, Blueprint, url_for
from app.login.form import LoginForm
import logging
from flask_login import logout_user

blue = Blueprint('', __name__, template_folder = 'templates')

@blue.route('/', methods = ['GET', 'POST'])
@blue.route('/index', methods = ['GET','POST'])
def index():
    site_title = 'School MS'
    my_h1_title = 'Welcome to KNUST BASIC SCHOOL'
    user = {'username':'Kaunda'}

    posts = [
            {

                'author':{'username':'Kaunda'}
                ,'title':'Post from Kaunda'
                ,'body':'This is the content of Kaunda'
            },
            {
                'author':{'username':'jinjiwa'}
                ,'title':'Post from Jinjiwa'
                ,'body':'This is the content of Jinjiwa'
            },

            {
                'author':{'username':'wiseking'}
                ,'title':'Post from wiseking'
                ,'body':'This is the content of Wiseking'
            },

            {
                'author':{'username':'Battuta'}
                ,'title':'Post from Battuta'
                ,'body':'This is the content of Battuta'
            },

            {
                'author':{'username':'Lamin'}
                ,'title':'Post from Lamin'
                ,'body':'This is the content of Lamin'
            },

            {
                'author':{'username':'Mansura'}
                ,'title':'Post from Mansura'
                ,'body':'This is the content of Mansura'
            },

            {
                'author':{'username':'Kande'}
                ,'title':'Post from Kande'
                ,'body':'This is the content of Kande'
            },

    ]
    logging.warning('See this message in the debugger tool bar. Testing DebugToolbarExtension')

    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/admin')
    return render_template('main/index.html'
                        , site_title = site_title
                        , my_h1_title=my_h1_title
                        , user = user
                        , posts = posts, form = form)


#user logout
@blue.route('/logout', methods = ['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login.login'))
