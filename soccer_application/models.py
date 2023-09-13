from flask_login import UserMixin
from soccer_application import db, login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id)) 


players_in_games = db.Table('player_in_games',
    db.Column('game_id', db.Integer, db.ForeignKey('games.id')),
    db.Column('player_id', db.Integer, db.ForeignKey('players.id')),
    db.Column('created_at', db.DateTime),
    db.Column('participate', db.Boolean)
)

fans = db.Table('fans',
    db.Column('player_id', db.Integer, db.ForeignKey('players.id')),
    db.Column('fav_team_id', db.Integer, db.ForeignKey('favoriteteams.id'))
)

class Games(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_date=db.Column(db.DateTime,nullable=False)
    team_id=db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    court_id=db.Column(db.Integer, db.ForeignKey('courts.id'), nullable=False)
    
    def __repr__(self):
        return f"Game(game_id: '{self.id}','{'at'}','{self.game_date}')"

class FavoriteTeams(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_name=db.Column(db.String(50))
    country=db.Column(db.String(50))
    
    def __repr__(self):
        return f"Favorite Team('{self.team_name}')"


class Courts(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(100),nullable=False)
    address=db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f"Court(court_name: '{self.name}','{'at'}','{self.address}')"


class Teams(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(100),nullable=False)
    players=db.relationship('Players', backref='teams', lazy=True)
    
    def __repr__(self):
        return f"Team('{self.name})"
    
class Expenses(db.Model):
    __table_args__ = (
        db.CheckConstraint(db.amount >= 0, name='check_amount_positive')
    )
    id=db.Column(db.Integer, primary_key=True, autoincerement=True)
    date=db.Column(db.DateTime)
    amount=db.Column(db.Integer)
    description=db.Column(db.String(200))
    team_id=db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

class Payments(db.Model):
    __table_args__ = (
        db.CheckConstraint(db.amount >= 0, name='check_amount_positive')
    )
    id=db.Column(db.Integer, primary_key=True, autoincerement=True)
    date=db.Column(db.DateTime)
    amount=db.Column(db.Integer)
    team_id=db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    player_id=db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)

class Users(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at=db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at=db.Column(db.DateTime, nullable=True)
    username=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(50), nullable=False)
    contact_info = db.relationship('ContactInfo', backref='user', lazy=True, uselist=False)
    #profile_image=db.Column(db.String(200),default='#path to default jpeg.')
        
    def __repr__(self):
        return f"User('{self.username}')"
    
class ContactInfo(db.Model):
    __table_args__=(
         db.CheckConstraint('NOT(phone IS NULL AND email IS NULL)')
    )

    id=db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    phone=db.Column(db.String(25))
    email=db.Column(db.String(40))


class Managers(Users):
    id=db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
        
    def __repr__(self):
        return f"Manager('{self.id}')"

class Player(Users):
    id=db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    first_name=db.Column(db.String(50),nullable=False)
    last_name=db.Column(db.String(50),nullable=False)
    date_of_birth=db.Column(db.DateTime,nullable=False)
    status=db.Column(db.Boolean,nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    #profile_image=db.Column(db.String(20),nullabale=False,default='default.jpg')

    def __repr__(self):
            return f"Player('{self.first_name}',' ','{self.last_name}')"
