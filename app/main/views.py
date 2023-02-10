from app import db
from app.models import User
from . import main
from .forms import LoginForm

from flask import render_template, redirect, url_for, flash
from flask_login import login_required, login_user, current_user, logout_user


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/login/', methods=['post', 'get'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('.admin'))

        flash("Invalid username/password", 'error')
        return redirect(url_for('.login'))
    return render_template('login.html', form=form)


