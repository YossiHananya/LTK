from flask import Blueprint, request, render_template, url_for, flash, redirect
from flask_login import login_user, logout_user, current_user, login_required
from .forms import RegistrationForm, LoginForm, UpdateProfileForm
from .. import db, bcrypt
from ..models import User

users = Blueprint('users', __name__)

@users.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
        
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
        flash(f'Account created for {form.username.data}!', 'success')

        login_user(user, remember=form.remember.data)
        return redirect(url_for('main.index'))
    
    return render_template('register.html',title='Register',form=form)

@users.route("/login",methods=['GET','POST'])
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
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        
    return render_template('login.html',title='Login',form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@users.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()

    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        flash("Profile was updated successfully", 'success')

        return redirect(url_for('main.index'))

    if request.method == 'GET':
        form.username.data = current_user.username

    return render_template('profile.html', title='Profile', form = form)
