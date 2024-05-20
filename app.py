import os
from flask import Flask , request, jsonify
from models import setup_db, Movies, Actors
from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def casting_team():
        movies = Movies.query.all()
        actors = Actors.query.all()
        result = "<h1>Upcoming Movies</h1>"
        for movie in movies:
            result += f"<p>Title: {movie.title}, Release Date: {movie.release_date}</p>"
        result += "<h1>Casting Team Qualified Actors</h1>"
        for actor in actors:
            result += f"<p>Name: {actor.name}, Age: {actor.age}, Gender: {actor.gender}</p>"
        return result 

    @app.route('/actors', methods=['GET'])
    def get_actors():
        actor = Actors.query.all()
        result = []
        for actors in actor:
            actor_data = {
                'id' : actors.id,
                'name': actors.name,
                'age': actors.age,
                'gender': actors.gender
            }
            result.append(actor_data)
        return jsonify(result), 200  


    @app.route('/actors', methods=['POST'])
    def add_actor():
        data = request.json
        new_actor = Actors(
            name=data['name'],
            age=data['age'],
            gender=data['gender']
        )
        new_actor.insert()
        return jsonify({'message': 'Actor added successfully'}), 201

    @app.route('/actors/<int:id>', methods=['DELETE'])
    def delete_actor(id):
        actor = Actors.query.get(id)
        if actor:
            actor.delete()
            return jsonify({'message': f'Actor with ID {id} deleted successfully'}), 200
        else:
            return jsonify({'error': f'Actor with ID {id} not found'}), 404

    @app.route('/actors/<int:id>', methods=['PATCH'])
    def update_actor(id):
        actor = Actors.query.get(id)
        if actor is None:
            return jsonify({'error': 'Actor not found'}), 404
        
        data = request.json

        if 'name' in data:
            actor.name = data['name']
        if 'age' in data:
            actor.age = data['age']
        if 'gender' in data:
            actor.gender = data['gender']

        actor.update()          

        return jsonify({'message': 'Actor updated successfully'}), 200    

    @app.route('/movies', methods=['GET'])
    def get_movies():
        movie = Movies.query.all()
        result = []
        for movies in movie:
            movie_data = {
                'id' : movies.id,
                'title': movies.title,
                'release_date': movies.release_date
            }
            result.append(movie_data)
        return jsonify(result), 200  


    @app.route('/movies', methods=['POST'])
    def add_movies():
        data = request.json
        new_movie = Movies(
            title=data['title'],
            release_date=data['release_date']
        )
        new_movie.insert()
        return jsonify({'message': 'Movies added successfully'}), 201

    @app.route('/movies/<int:id>', methods=['DELETE'])
    def delete_movies(id):
        movie = Movies.query.get(id)
        if movie:
            movie.delete()
            return jsonify({'message': f'Movies with ID {id} deleted successfully'}), 200
        else:
            return jsonify({'error': f'Movies with ID {id} not found'}), 404

    @app.route('/movies/<int:id>', methods=['PATCH'])
    def update_movies(id):
        movie = Movies.query.get(id)
        if movie is None:
            return jsonify({'error': 'Movie not found'}), 404
        
        data = request.json

        if 'title' in data:
            movie.title = data['title']
        if 'release_date' in data:
            movie.release_date = data['release_date']

        movie.update()          

        return jsonify({'message': 'Movie updated successfully'}), 200

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
