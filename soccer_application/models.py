
from soccer_application import db

event_player_association = db.Table('event_player_association',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'))
)

team_player_association = db.Table('team_player_association',
    db.Column('team_id', db.Integer, db.ForeignKey('team.id')),
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'))
)

team_manager_association = db.Table('team_manager_association',
    db.Column('team_id', db.Integer, db.ForeignKey('team.id')),
    db.Column('manager_id', db.Integer, db.ForeignKey('manager.id'))
)

team_location_association = db.Table('team_location_association',
    db.Column('team_id', db.Integer, db.ForeignKey('team.id')),
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'))
)

class Event(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    event_date=db.Column(db.DateTime,nullable=False)
    players=db.relationship('Player',secondary=event_player_association,backref='events')
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    
    def __repr__(self):
        return f"Event(location_id: '{self.location_id}','{'at'}','{self.event_date}')"


class Location(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False, unique=True)
    events=db.relationship('Event', backref='locations')
    
    def __repr__(self):
        return f"Location('{self.name})"


class Team(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String,nullable=False)
    players=db.relationship('Player',secondary=team_player_association,backref='teams')
    locations=db.relationship('Location',secondary=team_location_association, backref='locations')
    
    def __repr__(self):
        return f"Team('{self.name})"

class MainTeam(Team):
    __tablename__ = "mainteam"
    
    id=db.Column(db.Integer, db.ForeignKey('team.id'), primary_key=True)
    team = db.relationship('Team', backref='main_team')
    players=db.relationship('Player', backref='main_teams')

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


class Manager(User):
    id=db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    teams=db.relationship('Team',secondary=team_manager_association, backref='managers')
        
    def __repr__(self):
        return f"Manager('{self.id}')"

class Player(User):
    id=db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)    
    first_name=db.Column(db.String,nullable=False)
    last_name=db.Column(db.String,nullable=False)
    gender=db.Column(db.String,nullable=True)
    main_team_id = db.Column(db.Integer, db.ForeignKey('mainteam.id'), nullable=False)
    #image_file=db.Column(db.String(20),nullabale=False,default='default.jpg')

    def __repr__(self):
            return f"Player('{self.first_name}',' ','{self.last_name}')"
