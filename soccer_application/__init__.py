from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from .config.config import Config
import os
from .config.config_names import ConfigName

db=SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_name=ConfigName.DEVELOPMENT):
    app = Flask(__name__)
    config=Config.from_type(config_value=config_name)
    db_dir_path = config.get('APP_CONFIG', {}).get('DATABASE_DIR', path.dirname(__file__))
    db_path = path.join(db_dir_path, config.get('APP_CONFIG')['DATABASE_URI'])
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{db_path}'
    app.config.update(config.get('APP_CONFIG'))

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.login_message_category = 'info'

    with app.app_context():
        db.create_all()

    from .main.routes import main
    from .users.routes import users
    app.register_blueprint(main)
    app.register_blueprint(users)

    return app
