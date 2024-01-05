from wtforms import StringField, TextAreaField, PasswordField, SubmitField, IntegerField, validators, Form, ValidationError
from flask_wtf.file import FileRequired, FileAllowed, FileField
from flask_wtf import FlaskForm
from .models import RegisterModel

class CustomerRegistrationForm(FlaskForm):
    name = StringField('Name')
    username = StringField('Username')
    email = StringField("Email")
    password = PasswordField('Password', [ validators.EqualTo('confirm', message="Both passwords should match")])
    confirm = PasswordField("Repeat Password")
    country = StringField('Country')
    state = StringField('State')
    city = StringField('City')
    contact = StringField('Contact')
    address = StringField('Address')

    profile_image = FileField("Profile Image", validators=[FileAllowed(['jpg', 'png', 'jpeg'], "Images only")])
    
    submit = SubmitField("Register")

    def validate_username(self, username):
        if RegisterModel.query.filter_by(username=username.data).first():
            raise ValidationError("Username already Exists.")

    def validate_email(self, email):
        if RegisterModel.query.filter_by(email=email.data).first():
            raise ValidationError("Email already Exists.")

class CustomerLoginForm(FlaskForm):
    email = StringField("Email")
    password = PasswordField('Password')