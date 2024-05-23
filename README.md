# FSND Captone Project

It's a Full stack ND project by Udacity. project is based on casting agency which allow user to CREATE, UPDATE, READ, DELETE of Actors and Movies.


**Environment Setup**

**Local**

```
# Change to project folder
cd Path user/udacity/project etc
```

**Initialize and activate a virtualenv using:**
```
# Mac Users

python3.8 -m venv env
source env/bin/activate
```
**Install the dependencies:**
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

**Run the development server:**

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

**API Reference**

### Roles:

- Casting Assistant

	- Can view actors and movies

- Casting Director

	- All permissions a Casting Assistant has and…
	- Add or delete an actor from the database
	- Modify actors or movies

- Executive Producer

	- All permissions a Casting Director has and…
	- Add or delete a movie from the database

### Set Permissions:

    - `delete:actors`
    - `delete:movies`
    - `get:actors`
    - `get:movies`
    - `patch:actors`
    - `patch:movies`
    - `post:actors`
    - `post:movies`

### Set JWT Tokens