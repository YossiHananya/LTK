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
    db_path = path.join(path.dirname(__file__), config.get('APP_CONFIG')['DATABASE_URI'])
    app.config.update(config.get('APP_CONFIG'))
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{db_path}'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.login_message_category = 'info'

    with app.app_context():
        from . import api
        db.create_all()

    return app