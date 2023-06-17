from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='77c047c61ee454616ae47f76410bf10b'
db_path = path.join(path.dirname(__file__), 'site.db')
app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{db_path}'
app.app_context().push()
db=SQLAlchemy(app)

from soccer_application import api

db.create_all()