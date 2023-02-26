from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'main.login'


def page_not_found(e):
    return render_template('404.html'), 404


def create_app(config):
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
