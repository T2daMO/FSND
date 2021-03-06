import os
from flask import Flask, request, abort, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category
from flask.templating import render_template
from backend import test_flaskr


QUESTIONS_PER_PAGE = 10


def paginate_questions(request, questions):
    page = request.args.get('page',1,type=int)
    start_Page = (page - 1) * QUESTIONS_PER_PAGE
    end_Page = start_Page + QUESTIONS_PER_PAGE
    
    formated_questions = [question.format() for question in questions]
    current_questions = formated_questions[start_Page:end_Page]
    return current_questions

def paginate_categories(request, categories): 
    page = request.args.get('page',1,type=int)
    start_Page = (page - 1) * QUESTIONS_PER_PAGE
    end_Page = start_Page + QUESTIONS_PER_PAGE
    
    formated_questions = [category.format() for category in categories]
    current_categories = formated_questions[start_Page:end_Page]
    return current_categories

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
        formated_categories = paginate_categories(request, categories)
        
        if len(formated_categories)==0:
            abort(404)

        return jsonify({
            'Success':True,
            'Categories':formated_categories,
            'Total number of categories': len(categories)
            })

    @app.route('/questions')
    def retreive_questions():
        questions = Question.query.all()
        current_questions = paginate_questions(request, questions)
        
        if len(questions) == 0:
            abort(404)     
        return jsonify({
                'Success':True,
                'Question':current_questions,
                'total_questions':len(questions),
                })

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id==question_id).one_or_none()
    
            if question == None:
                abort(404)
                
            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)
            return jsonify({
                'success':True,
                'deleted':question_id,
                'Question':current_questions,
                'total_questions':len(Question.query.all())
                })
        except:
            abort(422)

    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()
        
        new_question = body.get('question',None)
        new_answer = body.get('answer',None)
        new_type = body.get('category', None)
        new_difficulty = body.get('difficulty', None)
        new_category = body.get('type',None)
        
        try:
            new_category_id = Category.query.filter_by(id=new_category).first()
            new_category_name = Category.query.filter_by(id=new_type).first()
            question = Question(question=new_question, answer=new_answer, category=new_category_name.type,
                                difficulty=new_difficulty,category_id=new_category_id.id)
            question.insert()
            selection = Question.query.all()
            current_questions = paginate_questions(request, selection)
            return jsonify({
                'Success' :True,
                'Total_questions':len(Question.query.all()),
                'questions':current_questions
               })
        except:
            abort(422)
            
    @app.route('/questions/<search>', methods=['POST'])    
    def get_apecific_question(search):
        questions = Question.query.filter_by(Question.question.ilike('%{}%'.format(search))).all()
        current_questions = paginate_questions(request, questions)
        
        if len(questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'question': current_questions,
            'total_questions': len(current_questions)
            })

    @app.route('/questions/<category>', methods=['GET'])
    def get_question_by_category(category):
        new_category_name = Question.query.filter_by(category=category).all()
        current_questions = paginate_questions(request, new_category_name)
        
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
    @app.route('/questions/quiz/<category>', methods=['POST'])
    def get_quiz_questions():
        question = Question.query.filter_by(category=category).all()
        previous_question = paginate_questions(request, question)
        
        random.shuffle(questions)
        session['previous_question'] = previous_question
        if 'previous_question' in session:
            return jsonify({"Success": True})
        else:
            return jsonify({'Success': False})
        
        return jsonify({
            'success': True,
            'question': previous_question
            })
       
    '''
    @TODO: 
    Create error handlers for all expected errors 
    including 404 and 422. 
    '''
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'Success':False,
            'Error':400,
            'Message':"Bad request"
            },400)
      
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'Success':False,
            'Error':404,
            'Message':"Resource not found!"
            },404)
        
    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            'Success':False,
            'Error':405,
            'Message':"Method not allowed!"
            },405)
    
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'Success':False,
            'Error':422,
            'Message':"Unprocessable entity!"
            },422)       

    return app
    
    