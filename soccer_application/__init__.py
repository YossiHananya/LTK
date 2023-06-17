from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='77c047c61ee454616ae47f76410bf10b'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
app.app_context().push()
db=SQLAlchemy(app)