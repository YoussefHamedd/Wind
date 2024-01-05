from wtforms import StringField, Form, StringField, BooleanField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField("Name")
    username = StringField("Username")
    email = StringField("Email")
    password = PasswordField("New Password", [
        validators.EqualTo('confirm', message="Passwords must match")
    ])
    confirm = PasswordField("Repeat Password")

class LoginForm(Form):
    email = StringField("Email")
    password = PasswordField("Password")