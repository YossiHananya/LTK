from flask import Flask, jsonify, request
    
app=Flask(__name__)


players_list=[
    { 'name': 'Assaf', 'team': 1 }
]

@app.route('/players')
def get_players():
    return jsonify(players_list)

@app.route('/players',methods=['POST'])
def register_player():
    player_data=request.get_json()
    players_list.append(player_data)
    response = {'message': 'Player added successfully'}
    return jsonify(response), 200
