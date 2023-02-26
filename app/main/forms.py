from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import PasswordInput


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", widget=PasswordInput(hide_value=False),
                           validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField()


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", widget=PasswordInput(hide_value=False),
                           validators=[DataRequired()])
    email = StringField("Email", validators=[Email()])
    remember = BooleanField("Remember Me")
    submit = SubmitField()


class DeleteForm(FlaskForm):
    password = StringField("Password", widget=PasswordInput(hide_value=False),
                           validators=[DataRequired()])
    submit = SubmitField()
