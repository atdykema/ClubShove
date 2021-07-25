from flask_wtf import Form
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import EqualTo, InputRequired

class SignUpForm(Form):
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    password_verify = PasswordField('Verify password', validators=[EqualTo(password)])
    submit = SubmitField('Login')