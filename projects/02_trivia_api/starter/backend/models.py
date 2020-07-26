import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy.orm import backref


database_name = "trivia"
database_path = "postgres://{}:{}@{}/{}".format('postgres','password1','localhost:5432',database_name)
db = SQLAlchemy()

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

'''
Question

'''
class Question(db.Model):
    __tablename__ = 'questions'
    
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    category = Column(String)
    difficulty = Column(Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    
    def __init__(self, question, answer, category, difficulty, category_id):
        self.question = question
        self.answer = answer
        self.category = category
        self.difficulty = difficulty
        self.category_id = category_id
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
          'id': self.id,
          'question': self.question,
          'answer': self.answer,
          'category': self.category,
          'difficulty': self.difficulty,
          'category_id': self.category_id
          }

'''
Category

'''
class Category(db.Model):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    type = Column(String)
#     question_id = db.relationship('Question', backref=backref('Category', order_by=id))
        
    def __init__(self, type):
        self.type = type
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def format(self):
        return {
          'id': self.id,
          'type': self.type
        }