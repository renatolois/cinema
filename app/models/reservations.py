from app import db


reservations = db.Table (
    'reservations',
    db.Column( 'user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True ),
    db.Column( 'movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True )
)