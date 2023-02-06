import os

from app import db, create_app

from flask_migrate import MigrateCommand
from flask_script import Manager, Shell


def make_shell_context():
    return dict(app=app, db=db)


app = create_app(os.getenv('FLASK_ENV') or 'config.DevelopmentConfig')

manager = Manager(app)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
