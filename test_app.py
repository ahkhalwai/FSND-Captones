import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actors, Movies

test_database_path = os.environ['TEST_DATABASE_URL']

class FSNDTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "fsndtest"
        self.database_path = test_database_path
        self.ttoken = os.getenv('TEST_TOKEN')
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_actors(self):
        res = self.client().get("/actors", headers={
                'Authorization': self.ttoken})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"], True)
    
    def test_create_new_actors(self):
        self.new_actors = {
            "name": "Amir Khan",
            "age": 45,
            "gender": "Male"
        }
        
        res = self.client().post("/actors", json=self.new_actors, headers={
                'Authorization': self.ttoken})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"], True)

    # def test_delete_actors(self):
    #     res = self.client().delete("/actors/2", headers={
    #            'Authorization': self.ttoken})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertTrue(data["success"], True)    

    def test_update_actors(self):
        self.upd_actors = {
            "name": "Salman Khan"
        }
        
        res = self.client().patch("/actors/2", json=self.upd_actors, headers={
                'Authorization': self.ttoken})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"], True)
    
    def test_get_movies(self):
        res = self.client().get("/movies", headers={
                'Authorization': self.ttoken})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"], True)
    
    def test_create_new_movies(self):
        self.new_movies = {
            "title": "haryy grain",
            "release_date": "1996-03-31"
        }
        
        res = self.client().post("/movies", json=self.new_movies, headers={
                'Authorization': self.ttoken})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"], True)

    # def test_delete_actors(self):
    #     res = self.client().delete("/movies/3", headers={
    #            'Authorization': self.ttoken})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertTrue(data["success"], True)    

    def test_update_movies(self):
        self.upd_movies = {
            "title": "garry kaspersky"
        }
        
        res = self.client().patch("/movies/2", json=self.upd_movies, headers={
                'Authorization': self.ttoken})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"], True)
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()