import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

# paginating questions by paginate_questions() function


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # creating and configure the app
    app = Flask(__name__)
    setup_db(app)

    # Set up CORS. Allow '*' for origins
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Using the after_request decorator to set Access-Control-Allow

    @app.after_request
    def after_request(respons):
        '''seting access control'''
        respons.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization,true')
        respons.headers.add(
            'Access-Control-Allow-Methods',
            'GET, POST, PATCH, DELETE, OPTIONS')

        return respons

    @app.route('/categories', methods=['GET'])
    def get_categories():
        ''' handling GET requests for all available categories'''
        # get  all available categories
        categories = Category.query.order_by(Category.id).all()
        # formatted categories as dict
        categories_formatted = {
            category.id: category.type for category in categories}
        # abort if there is no retrived categories
        if len(categories) == 0:
            abort(404)
        # return categories by this endpoint to view
        return jsonify({'success': True, 'categories': categories_formatted})

    @app.route('/questions', methods=['GET'])
    def get_all_questions():
        '''handling GET requests for questions with  pagination (every 10 questions)'''
        # get all questions
        try:
            questions = Question.query.order_by(Question.id).all()
            # formatted questions as list with pagination
            questions_formatted = paginate_questions(request, questions)
            # get all categories
            categories = Category.query.order_by(Category.id).all()
            # formatted categories as dict
            categories_formatted = {
                category.id: category.type for category in categories}
            # abort if there are no retrived categories
            if (len(questions_formatted) == 0):
                abort(404)
            # return a list of questions,number of total questions, current
            # category, categories to view
            return jsonify({'success': True,
                            'categories': categories_formatted,
                            'questions': questions_formatted,
                            'total_questions': len(questions)})
        except BaseException:
            abort(400)

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        '''handling DELETE requests for deleting question using an id of the question '''
        try:
            # get the selected question by id
            question = Question.query.filter(
                Question.id == question_id).one_or_none()
            # abort if there are no retrived question
            if question is None:
                abort(404)
            # delete question from database
            question.delete()
            # return data to view
            return jsonify({'success': True, 'Deleted': question_id})
        except BaseException:
            abort(422)

    @app.route('/questions', methods=['POST'])
    def insert_question():
        '''handling POST requests to add a new question'''
        # load data of request body as json and assign it to variables
        body = request.get_json()
        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_category = body.get('category')
        new_difficulty = body.get('difficulty')
        # abort if there are no new question and  new answer
        if new_question is None or new_answer is None or new_question is "" or new_answer is "":
            abort(404)
        try:
            # insert new question to database
            question = Question(
                question=new_question,
                answer=new_answer,
                category=new_category,
                difficulty=new_difficulty)
            question.insert()
            return jsonify({'success': True})

        except BaseException:
            abort(422)

    @app.route('/searches', methods=['POST'])
    def search_for_question():
        '''handling POST requests to get questions based on a search term'''
        # load data of request body as json and assign it to variables
        body = request.get_json()
        search = body.get('searchTerm', None)
        try:
            if search:
                # retrive the question including on search term
                results = Question.query.order_by(Question.id).filter(
                    Question.question.ilike(f'%{search}%')).all()
                # formmated retrived questions as a list
                formmated_questions = [question.format()
                                       for question in results]
                # save number of categories of questions as list
                current_category = [question['category']
                                    for question in formmated_questions]
                # return required data to view
                return jsonify({
                    'success': True,
                    "questions": formmated_questions,
                    "total_questions": len(formmated_questions),
                    "current_category": current_category
                })
            else:
                abort(404)
        except BaseException:
            abort(422)

    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_catogrized_question(category_id):
        '''handleing GET request to get questions based on category'''
        # retrive selected category
        catogry = Category.query.filter(
            Category.id == category_id).one_or_none()
        # abort if retriveed catogry is None
        if catogry is None:
            abort(404)
        try:
            # retrive questions blong to selected catogry
            questions = Question.query.order_by(
                Question.id).filter(
                Question.category == catogry.id).all()
            # formatted questions and paginate it
            questions_formatted = paginate_questions(request, questions)
            # retrun required data to view
            return jsonify({'success': True,
                            'current_category': catogry.id,
                            'questions': questions_formatted,
                            'total_questions': len(questions)})
        except BaseException:
            abort(500)

    @app.route('/quizzes', methods=['POST'])
    def play_quizzes():
        ''' handleing POST request to get questions to play the quiz'''
        # load data of request body as json and assign it to variables
        body = request.get_json()
        previous = body.get('previous_questions', [])
        quiz_category = body.get('quiz_category', None)
        try:
            # if catogry not none made quize
            if quiz_category:
                # retrive  questions according to catogry
                if quiz_category['id'] != 0:
                    questions = Question.query.filter(
                        Question.id.notin_(previous),
                        Question.category == quiz_category['id']).all()
                # retrive  all questions
                else:
                    questions = Question.query.filter(
                        Question.id.notin_(previous)).all()
                # formatted selected questions as list
                formatted_questions = [question.format()
                                       for question in questions]
                # This condition to give score  if all questions in the
                # previous and it less than 5
                if(len(formatted_questions) == 0):
                    # retrun data to view
                    return jsonify({'success': True, 'question': None})
                else:
                    # selected random question of list question
                    random_question = random.choice(formatted_questions)
                    if random_question:
                        # retrun data to view
                        return jsonify(
                            {'success': True, 'question': random_question})
                    else:
                        # retrun data to view
                        return jsonify({'success': True, 'question': None})
            # if catogry none abort
            else:
                abort(400)
        except BaseException:
            abort(422)

    # error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    return app
