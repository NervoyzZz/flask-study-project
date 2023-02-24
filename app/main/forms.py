from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField()


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    email = StringField("Email", validators=[Email()])
    remember = BooleanField("Remember Me")
    submit = SubmitField()


class DeleteForm(FlaskForm):
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField()
