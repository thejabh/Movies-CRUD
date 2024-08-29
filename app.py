"""
create web app
create env for python 3.7
upload files in that env
pip install modules try deployinfg



"""
from flask import Flask, flash,render_template,redirect,request,url_for,flash,jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db,Movie,MovieActors,MovieGenres,MovieTechnicians,Actor,Genre,Technician

app=Flask(__name__)
app.secret_key="Secret Key"

"""
    Configuration
    SQLALCHEMY DATABASE URL = mysql://root:'1234'@localhost/moviesdb
    SQLALCHEMY TRACK MODIFICATIONS = False
"""
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:1234@localhost/moviesdb"
# app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://ThejaBH:database@ThejaBH.mysql.pythonanywhere-services.com/ThejaBH$moviesdb"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# @app.on_server_startup
def initdb():
    db.create_all()
    
    genres = ['Action', 'Comedy', 'Drama', 'Sci-fi', 'Romance', 'Horror']
    for genre_name in genres:
        genre = Genre.query.filter_by(name=genre_name).first()
        if not genre:
            genre = Genre(name=genre_name)
            db.session.add(genre)
    
    
    
    db.session.commit()
    print('Initialized the database and prepopulated with genres .')



@app.route('/')
def home():
    all_movies = Movie.query.all()
    actors={}
    genres={}
    technicians={}
    for movie in all_movies:
        actors_in_movie = MovieActors.query.filter_by(movie_id=movie.id)
        list_actors=[]
        for actor in actors_in_movie:
            list_actors.append( Actor.query.filter_by(id=actor.actor_id).first().name )
        actors[movie.id] =list_actors

        genres_of_movie = MovieGenres.query.filter_by(movie_id=movie.id).first()
        if genres_of_movie:
            genres[movie.id] = Genre.query.filter_by(id=genres_of_movie.genre_id).first().name
        list_technicians={}
        movie_technician = MovieTechnicians.query.filter_by(movie_id=movie.id)
        for tech in movie_technician:
            name = Technician.query.filter_by(id=tech.technician_id).first().name
            role = Technician.query.filter_by(id=tech.technician_id).first().role 
            list_technicians[role]=name
        technicians[movie.id]=list_technicians
    # print(technicians)
    # print(actors)
    # print(genres)
    return render_template('index.html',movies=all_movies,actors_list=actors,genres=genres,technicians=technicians,genredb={genre.id:genre.name for genre in Genre.query.all()})



@app.route('/insert',methods=['GET','POST'])
def insert():
    if request.method=='POST':
        movie_name = request.form.get('movie_name')
        year_of_release = request.form.get('year_of_release')
        user_rating = request.form.get('user_rating')
        genres = request.form.getlist('genres')  # Assuming these are the names of the genres
        actors = request.form.getlist('actors[]')
        director = request.form.get('director')
        producer = request.form.get('producer')
        cinematographer = request.form.get('cinematographer')
        editor = request.form.get('editor')

        # Create the Movie object
        new_movie = Movie(
            name=movie_name,
            year_of_release=int(year_of_release),
            user_rating=float(user_rating)
        )

        # Add genres
        for genre_name in genres:
            genre = Genre.query.filter_by(name=genre_name).first()
            new_movie.genres.append(genre)

        # Add actors
        for actor_name in actors:
            if actor_name!='':
                actor = Actor.query.filter_by(name=actor_name).first()
                if not actor :
                    actor = Actor(name=actor_name)
                new_movie.actors.append(actor)
        
        # Add technicians
        technicians = []

        # Director
        director_technician = Technician.query.filter_by(role='Director', name=director).first()
        if not director_technician:
            director_technician = Technician(role='Director', name=director)
        technicians.append(director_technician)

        # Producer
        producer_technician = Technician.query.filter_by(role='Producer', name=producer).first()
        if not producer_technician:
            producer_technician = Technician(role='Producer', name=producer)
        technicians.append(producer_technician)

        # Cinematographer
        cinematographer_technician = Technician.query.filter_by(role='Cinematographer', name=cinematographer).first()
        if not cinematographer_technician:
            cinematographer_technician = Technician(role='Cinematographer', name=cinematographer)
        technicians.append(cinematographer_technician)

        # Editor
        editor_technician = Technician.query.filter_by(role='Editor', name=editor).first()
        if not editor_technician:
            editor_technician = Technician(role='Editor', name=editor)
        technicians.append(editor_technician)

        new_movie.technicians.extend(technicians)

        # Add the new movie to the session and commit it to the database
        db.session.add(new_movie)
        db.session.commit()
        flash('Movie Inserted Successfully')
        return redirect(url_for('home'))


@app.route('/update',methods=['GET','POST'])
def update():

    if request.method=='POST':
        movie = Movie.query.get_or_404(request.form.get('id'))
        movie.name = request.form.get('movie_name')
        movie.year_of_release = int(request.form.get('year_of_release'))
        movie.user_rating = float(request.form.get('user_rating'))
        
        # Update genres
        selected_genres = request.form.getlist('genres')
        movie.genres.clear() 
        for genre_name in selected_genres:
            genre = Genre.query.filter_by(name=genre_name).first()
            movie.genres.append(genre)
        
        # Update actors
        actor_names = request.form.getlist(f'actors[]')
        print(actor_names)
        movie.actors.clear()
        for actor_name in actor_names:
            
            actor = Actor.query.filter_by(name=actor_name).first()
            if not actor and actor_name!='':
                actor = Actor(name=actor_name)
            movie.actors.append(actor)
        # Update technicians
        director = request.form.get('director')
        producer = request.form.get('producer')
        cinematographer = request.form.get('cinematographer')
        editor = request.form.get('editor')
        
        # Clear existing technicians and update with new ones
        movie.technicians.clear()
        technicians = []

        # Director
        director_technician = Technician.query.filter_by(role='Director', name=director).first()
        if not director_technician:
            director_technician = Technician(role='Director', name=director)
        technicians.append(director_technician)

        # Producer
        producer_technician = Technician.query.filter_by(role='Producer', name=producer).first()
        if not producer_technician:
            producer_technician = Technician(role='Producer', name=producer)
        technicians.append(producer_technician)

        # Cinematographer
        cinematographer_technician = Technician.query.filter_by(role='Cinematographer', name=cinematographer).first()
        if not cinematographer_technician:
            cinematographer_technician = Technician(role='Cinematographer', name=cinematographer)
        technicians.append(cinematographer_technician)

        # Editor
        editor_technician = Technician.query.filter_by(role='Editor', name=editor).first()
        if not editor_technician:
            editor_technician = Technician(role='Editor', name=editor)
        technicians.append(editor_technician)

        
        movie.technicians.extend(technicians)
        
        # Save the changes to the database
        db.session.commit()

        return redirect(url_for('home'))


@app.route('/delete/<id>/',methods=['GET','POST'])
def delete(id):
    movie = Movie.query.filter_by(id=id).first()
    db.session.delete(movie)
    db.session.commit()
    flash('Movie Deleted Succesfully')

    return redirect(url_for('home'))

@app.route('/filter_movies',methods=['GET'])
def filter_movies():
    genre_filter = request.args.get('genre_filter')
    actor_filter = request.args.get('actor_filter')
    technician_filter = request.args.get('technician_filter')

    # Start with the base query
    query = db.session.query(Movie)
    # db.session.query(Movie).join(Movie.genres).filter(Genre.name == genre_name).all()
    # Apply filters based on the user's input
    if genre_filter:
        query = query.join(Movie.genres).filter(Genre.name == genre_filter)
    if actor_filter:
        query = query.join(Movie.actors).filter(Actor.name == actor_filter)
    if technician_filter:
        query = query.join(Movie.technicians).filter(Technician.name == technician_filter)

    # Fetch the filtered movies
    all_movies = query.all()
    actors={}
    genres={}
    technicians={}
    for movie in all_movies:
        actors_in_movie = MovieActors.query.filter_by(movie_id=movie.id)
        list_actors=[]
        for actor in actors_in_movie:
            list_actors.append( Actor.query.filter_by(id=actor.actor_id).first().name )
        actors[movie.id] =list_actors

        genres_of_movie = MovieGenres.query.filter_by(movie_id=movie.id).first()
        if genres_of_movie:
            genres[movie.id] = Genre.query.filter_by(id=genres_of_movie.genre_id).first().name
        list_technicians={}
        movie_technician = MovieTechnicians.query.filter_by(movie_id=movie.id)
        for tech in movie_technician:
            name = Technician.query.filter_by(id=tech.technician_id).first().name
            role = Technician.query.filter_by(id=tech.technician_id).first().role 
            list_technicians[role]=name
        technicians[movie.id]=list_technicians
    # Return the same page but with the filtered movies
    return render_template('index.html',movies=all_movies,actors_list=actors,genres=genres,technicians=technicians,genredb={genre.id:genre.name for genre in Genre.query.all()})


def delete_actors_not_in_any_movies():
    # Identify actors who are not associated with any movies
    actors_to_delete = db.session.query(Actor).outerjoin(MovieActors).filter(MovieActors.actor_id.is_(None)).all()
    if not actors_to_delete:
        return 0
    
    # Delete identified actors
    for actor in actors_to_delete:
        db.session.delete(actor)
    
    # Commit the changes to the database
    db.session.commit()
    return len(actors_to_delete)

@app.route('/delete_unassociated_actors', methods=['DELETE'])
def delete_unassociated_actors():
    try:
        no_of_deletes = delete_actors_not_in_any_movies()
        db.session.commit()
        if no_of_deletes==0:
            flash("No Addititonal Actors")
        else:
            flash("Unassociate Actors are deleted")
        return jsonify({'message': 'Unassociated actors deleted successfully.'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# runs at the start of the server
with app.app_context():
    initdb()
if __name__=="__main__":
    app.run(debug=True)