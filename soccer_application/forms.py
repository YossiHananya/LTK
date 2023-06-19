import re
from wtforms import StringField, PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,ValidationError,EqualTo
from flask_wtf import FlaskForm
from soccer_application.models import User

def check_password_strength(form, field):
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """
    password = field.data
    #Checking for number in password
    if re.search(r"\d",password) is None:
        raise ValidationError("Password must contain at least one number")
    #Checking for uppercase in password
    if re.search(r"[A-Z]", password) is None:
        raise ValidationError("Password must contain at least one uppercase")
    #Checking for uppercase in password
    if re.search(r"[a-z]", password) is None:
        raise ValidationError("Password must contain at least one lowecase")
    #Checking for symbol in password
    if re.search(r"\W", password) is None:
        raise ValidationError("Password must contain at least one symbol")
    

class RegistrationForm(FlaskForm):

    username=StringField('Username',
                         validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email',
                      validators=[DataRequired(),Email()])
    password=PasswordField('Password',
                           validators=[DataRequired(),Length(min=8),check_password_strength])
    password_confirmation=PasswordField('Confirm Password',
                                        validators=[DataRequired(),EqualTo('password')]) 
    submit=SubmitField('Sign Up')
    
    def validate_username(self, username):        
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("Username already exists")

    def validate_email(self, email):        
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Email already exists")


class LoginForm(FlaskForm):
    email=StringField('Email',
                      validators=[DataRequired(),Email()])
    password=PasswordField('Password',
                        validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')
    