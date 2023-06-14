
from soccer_application import db

event_player_association = db.Table('event_player_association',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'))
)

class Event(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    location=db.Column(db.String,nullable=False)
    event_date=db.Column(db.DateTime,nullable=False)
    players=db.relationship('Player',secondary=event_player_association,backref='events')

    def __repr__(self):
        return f"Event('{self.location}','{'at'}','{self.event_date}')"
    

class Player(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String,nullable=False)
    last_name=db.Column(db.String,nullable=False)
    #image_file=db.Column(db.String(20),nullabale=False,default='default.jpg')

    def __repr__(self):
        return f"Player('{self.first_name}',' ','{self.last_name}')"
