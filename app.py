import os
from flask import (
    Flask,
    request,
    abort,
    render_template,
    flash,
    session,
    redirect,
    url_for,
    jsonify
)
from models import setup_db, db_drop_and_create_all, Movies, Actors
from flask_cors import CORS, cross_origin
from auth import AuthError, requires_auth
from authlib.integrations.flask_client import OAuth
from urllib.parse import urlencode
import logging
logging.basicConfig(level=logging.DEBUG)

AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
AUTH0_BASE_URL = os.getenv('AUTH0_BASE_URL')
API_AUDIENCE = os.getenv('API_AUDIENCE')
AUTH0_CALLBACK_URL = os.getenv('AUTH0_CALLBACK_URL')
AUTH0_CLIENT_ID = os.getenv('AUTH0_CLIENT_ID')
AUTH0_CLIENT_SECRET = os.getenv('AUTH0_CLIENT_SECRET')
SECRET_KEY = os.getenv('SECRET_KEY')

def create_app(test_config=None):

    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.config['SECRET_KEY'] = SECRET_KEY
    setup_db(app)
    CORS(app)
    db_drop_and_create_all(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/')
    @cross_origin()
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
    @cross_origin()
    @requires_auth('get:actors')
    def get_actors(token):
        try:
            logging.debug("Fetching actors from the database")
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
            
            return jsonify({
                'success': True,
                'actors': result,
                'total_actors':len(result)
            }), 200  
        
        except Exception as e:
            app.logger.error('Error fetching actors: %s', str(e))
            return jsonify({
                'success': False,
                'error': str(e)
            })

    @app.route('/actors', methods=['POST'])
    @cross_origin()
    @requires_auth('post:actors')
    def add_actor(token):
        try:
            data = request.json
            new_actor = Actors(
                name=data['name'],
                age=data['age'],
                gender=data['gender']
            )
            new_actor.insert()
            return jsonify({
                'success': True,
                'message': 'Actor added successfully'
            }), 200

        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            })    

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @cross_origin()
    @requires_auth('delete:actors')
    def delete_actor(token,id):
        try:
            actor = Actors.query.get(id)
            if actor:
                actor.delete()
                return jsonify({
                    'success': True,
                    'message': f'Actor with ID {id} deleted successfully'
                    }), 200
            else:
                return jsonify({
                    'success': False,
                    'error': f'Actor with ID {id} not found'
                    }), 404

        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }) 

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @cross_origin()
    @requires_auth('patch:actors')
    def update_actor(token,id):
        try:
            actor = Actors.query.get(id)
            if actor is None:
                return jsonify({
                    'success': False,
                    'error': 'Actor not found'
                    })
            
            data = request.json

            if 'name' in data:
                actor.name = data['name']
            if 'age' in data:
                actor.age = data['age']
            if 'gender' in data:
                actor.gender = data['gender']

            actor.update()          

            return jsonify({
                'success': True,
                'message': 'Actor updated successfully'
                }), 200

        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            })             

    @app.route('/movies', methods=['GET'])
    @cross_origin()
    @requires_auth('get:movies')
    def get_movies(token):
        try:
            movie = Movies.query.all()
            result = []
            for movies in movie:
                movie_data = {
                    'id' : movies.id,
                    'title': movies.title,
                    'release_date': movies.release_date
                }
                result.append(movie_data)
            return jsonify({
                'success': True,
                'movies': result,
                'total_movies':len(result)
            }), 200  
        
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            })

    @app.route('/movies', methods=['POST'])
    @cross_origin()
    @requires_auth('post:movies')
    def add_movies(token):
        try:
            data = request.json
            new_movie = Movies(
                title=data['title'],
                release_date=data['release_date']
            )
            new_movie.insert()
            return jsonify({
                'success': True,
                'message': 'Movies added successfully'
                }), 200

        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            })

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @cross_origin()
    @requires_auth('delete:movies')
    def delete_movies(token,id):
        try:
            movie = Movies.query.get(id)
            if movie:
                movie.delete()
                return jsonify({
                    'success': True,
                    'message': f'Movies with ID {id} deleted successfully'
                    }), 200
            else:
                return jsonify({
                    'success': False,
                    'error': f'Movies with ID {id} not found'
                    }), 404

        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            })

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @cross_origin()
    @requires_auth('patch:movies')
    def update_movies(token,id):
        try:
            movie = Movies.query.get(id)
            if movie is None:
                return jsonify({
                    'success': False,
                    'error': 'Movie not found'
                    }), 404
            
            data = request.json

            if 'title' in data:
                movie.title = data['title']
            if 'release_date' in data:
                movie.release_date = data['release_date']

            movie.update()          

            return jsonify({
                'success': True,
                'message': 'Movie updated successfully'
                }), 200

        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            })

    '''
    # Error Handling
    '''

    @app.errorhandler(400)
    def badRequest(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
        }), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422
    
    @app.errorhandler(500)
    def serverError(error):
        app.logger.error('Server Error: %s', (error))
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code
    

    return app

app = create_app()
oauth = OAuth(app)

auth0 = oauth.register(
    'auth0',
    client_id=AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    api_base_url=AUTH0_BASE_URL,
    access_token_url='https://dev-aiehfurehuh6sbmf.us.auth0.com' +
    '/oauth/token',
    authorize_url='https://dev-aiehfurehuh6sbmf.us.auth0.com' +
    '/authorize',
    client_kwargs={
        'scope': 'openid profile email'})


@app.route('/login', methods=['GET'])
@cross_origin()
def login():
    print('Audience: {}'.format(API_AUDIENCE))
    return auth0.authorize_redirect(
        redirect_uri='%s/post-login' % AUTH0_CALLBACK_URL,
        audience=API_AUDIENCE
    )


@app.route('/post-login', methods=['GET'])
@cross_origin()
def post_login():
    token = auth0.authorize_access_token()
    session['token'] = token['access_token']
    print(session['token'])
    return render_template('pages/home.html'), 200


@app.route('/logout')
def log_out():
    session.clear()
    params = {
        'returnTo': url_for(
            'index',
            _external=True),
        'client_id': AUTH0_CLIENT_ID}
    return redirect(
        'https://dev-aiehfurehuh6sbmf.us.auth0.com' +
        '/v2/logout?' +
        urlencode(params))


if __name__ == '__main__':
    app.run()
