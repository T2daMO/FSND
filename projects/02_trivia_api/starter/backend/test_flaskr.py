import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres','password1','localhost:5432',self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        self.new_question = {
            'question':"What boxer's original name is Cassius Clay?",
            'answer':'Muhammad Ali',
            'dificulty':'1',
            'type':'History'
            }
        
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_paginated_questions(self):
        client_response = self.client().post('/questions')
        data = json.loads(client_response.data)
         
        self.assertEqual(client_response.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions'])) 
         
    def create_new_question(self):
        client_response = self.client().post('/question',json=self.new_question)
        data = json.loads(client_response.data)
         
        self.assertEqual(client_response.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['questions']))        
         
    def tes_get_paginated_questions(self):
        client_response = self.client().get('/questions')
        data = json.loads(client_response.data)
         
        self.assertEqual(client_response.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
          
    def test_get_paginated_categories(self):
        client_response = self.client().get('/categories')
        data = json.loads(client_response.data)
         
        self.assertEqual(client_response.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_categories'])
        self.assertTrue(len(data['categories']))         
          
    def test_404_requesting_page_over_limit(self):
        client_response = self.client().get('/questions?page=100',json={'questions':1})
        data = json.loads(client_response.data)
         
        self.assertEqual(client_response.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'resource not found')
         
    def test_405_if_question_creation_not_allowed(self):
        client_response = self.client().post('/questions/1000/',json=self.new_question)
        data = json.loads(client_response.data)
         
        self.assertEqual(client_response.status_code,405)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'method not allowed!')
        
    def test_search_questions_with_no_results(self):
        client_response = self.client().post('/questions',json={'search':'whose'})
        data = json.loads(client_response.data)
        
        self.assertEqual(client_response.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['total_questions'],0)
        self.assertEqual(data[len('questions')],0)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()