import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category
from flask.templating import render_template

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, questions):
    page = request.args.get('page',1,type=int)
    start_Page = (page - 1) * QUESTIONS_PER_PAGE
    end_Page = start_Page + QUESTIONS_PER_PAGE
    
    formated_questions = [questions for question in questions]
    current_questions = formated_questions[start_Page:end_Page]
    return current_questions 
  
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__,template_folder='C:/Commits/FSND/projects/02_trivia_api/starter/frontend/public')
    setup_db(app)
    CORS(app,resources={r"/api/*": {"origins": "*"}})
    
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authgorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE,OPTIONS')
        return response

    @app.route('/categories')
    def retreive_categories():
        categories = Category.query.all()
        formated_categories = paginate_questions(request, categories)
        
        if len(formated_categories)==0:
            abort(404)
      
        return jsonify({
            'Success':True,
            'Categories':formated_categories,
            'Total number of categories': len(categories)
            })

    @app.route('/questions', methods=['GET'])
    def retreive_questions():
        questions = Question.query.all()
        current_questions = [questions.format() for question in questions]

        current_questions = paginate_questions(request, questions)
        current_category = Category.query.all()
        
        if len(questions) == 0:
            abort(404)
               
        return jsonify({
                'Question':questions,
                'total_questions':len(Question.query.all()),
                'category': current_category
                })

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(id):
        try:
            question = Question.query.filter(Question.id == id).one_or_none()
            
            if question is None:
                abort(404)
            question.delete()
            
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)
            return jsonify({
                'deleted':id,
                'Question':current_questions,
                'total_questions':len(Question.query.all())
                })
        except:
            abort(422)
    '''
    @TODO: 
    Create an endpoint to POST a new question, 
    which will require the question and answer text, 
    category, and difficulty score.
    
    TEST: When you submit a question on the "Add" tab, 
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.  
    '''
    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()
        
        new_question = body.get('question',None)
        new_answer = body.get('answer',None)
        new_category = body.get('category', None)
        new_difficulty = body.get('difficulty', None)
        new_type = body.get('type',None)
        try:
            question = Question(question=new_question, answer=new_answer, category=new_category,difficulty=new_difficulty)
            question.insert()
            category = Category(type=new_type)
            category.insert()
            
            
            selection = Question.query.all()
            category_selection = Category.query.filter_by(selection.id).all()
            current_questions = paginate_questions(request, selection)
            return render_template('/index.html',jsonify({
                'Success' :True,
                'Total_questions':len(Question.query.all())
                }))
        except:
            abort(422)

    @app.route('/questions', methods=['POST'])    
    def get_specific_question():
        search = body.get('search',None)
        questions = Question.query.order_by(Question.id).filter_by(Question.question.ilike('%{}%'.format(search)))
        current_questions = paginate_questions(request, questions)
        
        if len(questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'question': current_questions,
            'total_questions': len(questions.all())
            })

    @app.route('/categories', methods=['GET'])
    def get_question_by_category():
        search = body.get('search',None)
        questions = Question.query.order_by(Question.id).filter_by(Question.category_id)
        current_questions = paginate_questions(request, questions)
        return jsonify({
            'success': True,
            'question': current_questions
            })
    
    '''
    @TODO: 
    Create a POST endpoint to get questions to play the quiz. 
    This endpoint should take category and previous question parameters 
    and return a random questions within the given category, 
    if provided, and that is not one of the previous questions. 
    
    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not. 
    '''
    @app.route('/quiz')
    def get_quiz_questions():
    
        return jsonify({})
       
    '''
    @TODO: 
    Create error handlers for all expected errors 
    including 404 and 422. 
    '''
    @app.errorhandler(400)
    def unprocessable(error):
        return jsonify({
            'Success':False,
            'Error':400,
            'Message':"Bad request"
            },400)
        
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'Success':False,
            'Error':422,
            'Message':"Unprocessable entity!"
            },422)
        
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'Success':False,
            'Error':404,
            'Message':"Resource not found!"
            },404)
        
    @app.errorhandler(405)
    def unprocessable(error):
        return jsonify({
            'Success':False,
            'Error':405,
            'Message':"Method not allowed!"
            },405)        

    
    return app
    
    