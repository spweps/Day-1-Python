from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import movie

class Director:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.year_born = data["year_born"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.movies = []

    @classmethod
    def get_directors_movies(cls):
        query = "SELECT * FROM directors JOIN movies ON directors.id = movies.director_id"
        all_directors_movies = connectToMySQL("directors_movies").query_db(query)
        directors_movies = []
    
        for dirmovs in all_directors_movies:
            dir_instance = Director(dirmovs)

            movie_data = {
                "id": dirmovs["movies.id"],
                "title": dirmovs["title"],
                "box_office": dirmovs["box_office"],
                "director_id": dirmovs["director_id"],
                "created_at": dirmovs["created_at"],
                "updated_at": dirmovs["updated_at"],
            }
            dir_instance.movie = movie.Movie(movie_data)

            directors_movies.append(dir_instance)
        return directors_movies
    
    @classmethod
    def get_director_movies(cls, data):
        query = "SELECT * FROM directors JOIN movies ON directors.id = movies.director_id where movies.director_id = %(id)s"
        all_directors_movies = connectToMySQL("directors_movies").query_db(query, data)
        
        director = Director(all_director_movies[0])
    
        for dirmovs in all_director_movies:
            movie_data = {
                "id": dirmovs["movies.id"],
                "title": dirmovs["title"],
                "box_office": dirmovs["box_office"],
                "director_id": dirmovs["director_id"],
                "created_at": dirmovs["created_at"],
                "updated_at": dirmovs["updated_at"],
            }
            director.movies.append(movie.Movie(movie_data))
        return director