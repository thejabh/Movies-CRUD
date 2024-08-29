from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Movies Table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    year_of_release = db.Column(db.Integer, nullable=False)
    user_rating = db.Column(db.Float, nullable=True)
    genres = db.relationship('Genre', secondary='movie_genres', backref='movies')
    actors = db.relationship('Actor', secondary='movie_actors', backref='movies')
    technicians = db.relationship('Technician', secondary='movie_technicians', backref='movies')
    
    def __init__(self,name,year_of_release,user_rating):
        self.name=name
        self.year_of_release=year_of_release
        self.user_rating=user_rating
        


# Genres Table
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

# Actors Table
class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

# Technicians Table
class Technician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(64), nullable=False)

# Association Tables
class MovieGenres(db.Model):
    __tablename__ = 'movie_genres'
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), primary_key=True)

class MovieActors(db.Model):
    __tablename__ = 'movie_actors'
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'), primary_key=True)

class MovieTechnicians(db.Model):
    __tablename__ = 'movie_technicians'
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), primary_key=True)
    technician_id = db.Column(db.Integer, db.ForeignKey('technician.id'), primary_key=True)
