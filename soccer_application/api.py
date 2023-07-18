import json
from flask import jsonify, request, render_template, url_for, flash, redirect, current_app as app
from flask_login import login_user, logout_user, current_user, login_required
from soccer_application import db, bcrypt
from soccer_application.forms import RegistrationForm, LoginForm, UpdateProfileForm
from soccer_application.models import Player, User

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! Please login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('Login Unsuccessful. Email does not exists','danger')
        elif not bcrypt.check_password_hash(user.password, form.password.data):
            flash('Login Unsuccessful. Incorrect Password','danger')
        else:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        
    return render_template('login.html',title='Login',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()

    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        flash("Profile was updated successfully", 'success')

        return redirect(url_for('index'))

    if request.method == 'GET':
        form.username.data = current_user.username

    return render_template('profile.html', title='Profile', form = form)
