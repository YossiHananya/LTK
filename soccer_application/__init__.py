from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import get_config

db=SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    config=get_config()
    app.config.from_object(config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    db_path = path.join(path.dirname(__file__), app.config['SQLALCHEMY_DATABASE_URI'])
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{db_path}'

    from soccer_application import api

    with app.app_context():
        db.create_all()

    return app