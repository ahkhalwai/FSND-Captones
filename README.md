# FSND Captone Project

It's a Full stack ND project by Udacity. project is based on casting agency which allow user to CREATE, UPDATE, READ, DELETE of Actors and Movies. [here](https://fsnd-captones.onrender.com)


## Environment Setup

### Local

```
# Change to project folder
cd Path user/udacity/project etc
```

#### Initialize and activate a virtualenv using:
```
# Mac Users

python3.8 -m venv env
source env/bin/activate
```
#### Install the dependencies:**
```
# run all required dependencies

pip3.8 install -r requirements.txt

# if any updates or install new dependencies so use this command to for updates the requirements.txt file.  

pip3.8 freeze > requirements.txt
```

```
chmod +x setup.sh
source setup.sh
echo $DATABASE_URL
echo $TEST_DATABASE_URL
echo $EXCITED
```

## Run the development server:

### Local

Main Project

```
export FLASK_APP=app.py;
export FLASK_ENV=development # enables debug mode
flask run --reload
```

Test Project

```
python3.8 test_app.py
```

### Render(Cloud)


#### Setup Roles on Auth0:

- Casting Assistant

	- Can view actors and movies

- Casting Director

	- All permissions a Casting Assistant has and…
	- Add or delete an actor from the database
	- Modify actors or movies

- Executive Producer

	- All permissions a Casting Director has and…
	- Add or delete a movie from the database

#### Set Permissions:

    - `delete:actors`
    - `delete:movies`
    - `get:actors`
    - `get:movies`
    - `patch:actors`
    - `patch:movies`
    - `post:actors`
    - `post:movies`

#### Set up Render PostgreSQL

- Create New PostgreSQL
- Once created copy `Internal database URL`

#### Set up Render Web Service

- Connect with Github project repo.
- Set up Environment like python version 3.8.12, excited true and database URL - paste the internal database url
- hit create button

#### Set up token from auth0

- once the render is live then only you can get token, now render is live so we go for token. 
- Update the callback url,logout url,web orgin, allowed orgins cors on application which we can copy from render web service url link and hit save button

```
https://{{YOUR_DOMAIN}}/authorize?audience={{API_IDENTIFIER}}&response_type=token&client_id={{YOUR_CLIENT_ID}}&redirect_uri={{YOUR_CALLBACK_URI}}

Example:
https://dev-aiehfurehuh6sbmf.us.auth0.com/authorize?audience=127.0.0.1:5000&response_type=token&client_id=fbycdYQo7Li69aDyq7zyAszlAwp5HLFn
&redirect_uri=https://render-deployment-examplesad.onrender.com
```

#### Set up render Environment and setup.sh final step for deployment

![Setup.sh](images/1.png)

![Render Environment](images/2.png)

## API Reference

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return the following error types when requests fail:
- 400: Bad Request
- 401: Unauthorized
- 404: Resource Not Found
- 422: Not Processable 
- 500: Internal Server Error

### Endpoints 

#### GET /actors

- get the actors.
- Returns: An object with a single key, `actors`, that contains a list of actors their name, age and gender.
- Sample: `curl -X GET -H "Content-Type: application/json" https://fsnd-captones.onrender.com/actors -H "Authorization: $TEST_TOKEN"`
```
{"actors":[{"age":39,"gender":"Female","id":1,"name":"Scarlett Johansson"},{"age":40,"gender":"Male","id":2,"name":"Chris Hemsworth"},{"age":48,"gender":"Male","id":3,"name":"Leonardo DiCaprio"},{"age":59,"gender":"Male","id":4,"name":"Keanu Reeves"}],"success":true,"total_actors":4}
```

#### POST /actors

- General:
    - Creates a new actor. 
- Sample: `curl -X POST -H "Content-Type: application/json" https://fsnd-captones.onrender.com/actors -H "Authorization: $TEST_TOKEN" --data-raw '{"name": "Salman Khan", "age": "45", "gender": "Male"}'`
```
{"message":"Actor added successfully","success":true}
```

#### DELETE /actors/id
- General:
    - Deletes the actor of the given ID if it exists.
- Sample: `curl -X DELETE -H "Content-Type: application/json" https://fsnd-captones.onrender.com/actors/2 -H "Authorization: $TEST_TOKEN"`
```
{"message":"Actor with ID 2 deleted successfully","success":true}
```

#### PATCH /actors/id
- General:
    - Updates the actor of the given ID if it exists.
- Sample: `curl -X PATCH https://fsnd-captones.onrender.com/actors/5 \
     -H "Authorization: $TEST_TOKEN" \
     -H "Content-Type: application/json" \
     --data-raw '{"name": "Amir Khan"}'
`
```
{"message":"Actor updated successfully","success":true}
```

#### GET /movies

- get the movies.
- Returns: An object with a single key, `movies`, that contains a list of actors their name, age and gender.
- Sample: `curl -X GET -H "Content-Type: application/json" https://fsnd-captones.onrender.com/movies -H "Authorization: $TEST_TOKEN"`
```
{"movies":[{"id":1,"release_date":"Fri, 18 Jul 2008 00:00:00 GMT","title":"The Dark Knight"},{"id":2,"release_date":"Fri, 16 Jul 2010 00:00:00 GMT","title":"Inception"},{"id":3,"release_date":"Wed, 31 Mar 1999 00:00:00 GMT","title":"The Matrix"},{"id":4,"release_date":"Mon, 31 Mar 1975 00:00:00 GMT","title":"The Gunman"}],"success":true,"total_movies":4}
```

#### POST /movies

- General:
    - Creates a new movies. 
- Sample: `curl -X POST https://fsnd-captones.onrender.com/movies \
     -H "Content-Type: application/json" \
     -H "Authorization: $TEST_TOKEN" \
     --data-raw '{ "title": "Avengers", "release_date": "2017-04-17" }'
`
```
{"message":"Movies added successfully","success":true}
```

#### DELETE /movies/id
- General:
    - Deletes the movies of the given ID if it exists.
- Sample: `curl -X DELETE -H "Content-Type: application/json" https://fsnd-captones.onrender.com/movies/1 -H "Authorization: $TEST_TOKEN"`
```
{"message":"Movies with ID 1 deleted successfully","success":true}
```

#### PATCH /movies/id
- General:
    - Updates the movies of the given ID if it exists.
- Sample: `curl -X PATCH https://fsnd-captones.onrender.com/movies/3 \
     -H "Authorization: $TEST_TOKEN" \
     -H "Content-Type: application/json" \
     --data-raw '{"title": "Anaconda"}'
`
```
{"message":"Movie updated successfully","success":true}
```
