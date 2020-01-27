from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')
