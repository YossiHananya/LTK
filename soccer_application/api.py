import json
from flask import jsonify, request, render_template
from soccer_application import app
from soccer_application.models import Player

@app.route("/")
@app.route("/home")
def index():
    return render_template('home.html', title='home', players=Player.query.all())

@app.route('/playersapi/players')
#Getting all players
def get_players():
    return {"Players":players}, 200

@app.route('/playersapi/players',methods=['POST'])
#Adding a new player to the list
def add_player():
    new_player = request.get_data() 
    players.append(json.loads(new_player.decode()))
    return jsonify({"message": "Player added successfully"}),201

@app.route("/playersapi/players/<int:player_id>", methods=['GET'])
def get_by_id(player_id:int):
    #Getting player information by ID
    for player in players:
        if player['id']==player_id:
            return jsonify({"Player_Details": player}),200
    return 
500
