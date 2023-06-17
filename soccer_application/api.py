import json
from flask import jsonify, request, render_template, url_for, flash, redirect
from soccer_application.forms import RegistrationForm,LoginForm
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

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'succes')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.html',title='Login',form=form)