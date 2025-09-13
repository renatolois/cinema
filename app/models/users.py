from app import db
from app.models.reservations import reservations


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column( db.Integer, primary_key = True )
    username = db.Column( db.String(25), nullable=False )
    email = db.Column( db.String(50), nullable=False, unique=True )
    movies = db.relationship('Movie', secondary=reservations, back_populates='users')