from flask import Blueprint, render_template
from ..models import Player

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def index():
    return render_template('home.html', title='home', players=Player.query.all())