from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from .config.config import Config
import os

db=SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__)
    config_dir = os.path.join(os.path.dirname(__file__), 'config')
    if config_name == 'dev':
        config_file = os.path.join(config_dir, 'dev.yaml')
    elif config_name == 'testing':
       config_file = os.path.join(config_dir, 'testing.yaml')
    else:
        raise ValueError(f"Invalid configuration name {config_name}")
    
    config=Config(config_file)
    db_path = path.join(path.dirname(__file__), config.get('APP_CONFIG')['DATABASE_URI'])
    app.config.update(config.get('APP_CONFIG'))
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{db_path}'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from soccer_application import api

    with app.app_context():
        db.create_all()

    return app