import os
from sqlalchemy import Column, Integer, Date, String, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy()
migrate = Migrate(db)

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

def db_drop_and_create_all(app):
    db.drop_all()
    db.create_all()

'''
Movies
Have title and release year
'''
class Movies(db.Model):  
  __tablename__ = 'Movies'

  id = Column(db.Integer, primary_key=True)
  title = Column(String)
  release_date = Column(Date)

  def __init__(self, title, release_date):
    self.title = title
    self.release_date = release_date

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date}
  
  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()   
  
  def delete(self):
    db.session.delete(self)
    db.session.commit()

'''
Actors
Have name, age and gender
'''

class Actors(db.Model):
  __tablename__ = 'Actors'
  
  id = Column(db.Integer, primary_key=True)  
  name = Column(String)
  age = Column(Integer)
  gender = Column(String)

  def __init__(self, name, age, gender):
      self.name = name
      self.age = age
      self.gender = gender

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender} 

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()   
  
  def delete(self):
    db.session.delete(self)
    db.session.commit()         
      
