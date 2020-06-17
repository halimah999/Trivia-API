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
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', '62328243', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.new_question = {
            'question': 'Is there new question for testing',
            'answer': 'yes',
            'category': 4,
            'difficulty': 1}

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

    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['categories']))

    def test_get_paginate_questions(self):
        """Testing the success of retriving questions and  paginating """
        # get the response and load the data
        res = self.client().get('/questions')
        data = json.loads(res.data)
        # check the status and success
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # check the corrected of return data
        self.assertTrue(data['categories'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])

    def test_400_send_requesting_beyond_valid_page(self):
        """Testing the faliur 404 of retriving questions and paginating """
        # get the response and load the data
        res = self.client().get('/questions?page=1000', json={'categories': 4})
        data = json.loads(res.data)
        # check the status and message
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_delete_question(self):
        """Testing the success  of delete selected question """
        # get the response and load the data
        res = self.client().delete('/questions/2')
        data = json.loads(res.data)
        # check the status and success
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # check the corrected of return data
        self.assertTrue('Deleted')

    def test_422_for_faild_delete(self):
        """Testing the faliur 422 of delete selected question"""
        # get the response and load the data
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)
        # check the status and message
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_insert_new_question(self):
        """Testing the success  of insert new question"""
        # get the response and load the data
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)
        # check the status and success
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_for_faild_create(self):
        """Testing the faliur 404  of insert new question"""
        # get the response and load the data
        res = self.client().post('/questions', json={})
        data = json.loads(res.data)
        # check the status and message
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_search_by_term(self):
        """Testing the success  of search based on term"""
        # get the response and load the data
        res = self.client().post('/searches', json={"searchTerm": "what"})
        data = json.loads(res.data)
        # check the status and success
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # check the corrected of return data
        self.assertTrue(len(data['current_category']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_422_for_faild_search(self):
        """Testing the faliur 422  of search based on term"""
        # get the response and load the data
        res = self.client().post('/searches', json={})
        data = json.loads(res.data)
        # check the status and message
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_quizze(self):
        """Testing the success  of play quiz"""
        # get the response and load the data
        res = self.client().post(
            '/quizzes',
            json={
                "previous_questions": [
                    12,
                    23],
                "quiz_category": {
                    "id": 4,
                    "type": "History"}})
        data = json.loads(res.data)
        # check the status and success
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_422_for_none_existance_category_in_quiz(self):
        """Testing the faliur 422  of of play quiz"""
        # get the response and load the data
        res = self.client().post(
            '/quizzes',
            json={
                "previous_questions": [
                    12,
                    23],
                "quiz_category": {}})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        # check the status and message
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_get_questions_of_categories(self):
        """Testing the success  of retrivequestion based on catogry"""
        # get the response and load the data
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        # check the status and success
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # check the corrected of return data
        self.assertTrue(len(data['questions']))
        self.assertTrue('total_questions')
        self.assertTrue('current_category')

    def test_404_requesting_beyond_valid_category(self):
        """Testing the faliur 404 of retrive question based on catogry"""
        # get the response and load the data
        res = self.client().get('/categories/100/questions')
        data = json.loads(res.data)
        # check the status and message
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
