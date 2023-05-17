from flask import Flask
    
app=Flask(__name__)

@app.route('/')
def index():
    return 'Hello User'

@app.route('/players')
def get_players():
    return []

@app.route('/players/register',methods=['POST'])
def register_player():
    return {}
