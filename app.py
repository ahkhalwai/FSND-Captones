import os
from flask import Flask
from models import setup_db, Movies
from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_movies():
        #excited = os.environ['EXCITED']
        movies = Movies.query.all()
        result = "<h1>Upcoming Movies</h1>"
        for movie in movies:
            result += f"<p>Title: {movie.title}, Release Date: {movie.release_date}</p>"
        return result

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
