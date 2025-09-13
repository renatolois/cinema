from app import db
from app.models.reservations import reservations


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column( db.Integer, primary_key=True )
    title = db.Column( db.String(30), nullable=False )
    description = db.Column( db.Text, nullable=False )
    location = db.Column( db.String(30), nullable=False )
    hour = db.Column( db.Time, nullable=False )
    users = db.relationship( 'User', secondary=reservations, back_populates='movies' )