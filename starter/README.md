# Full Stack API Final Project

## Full Stack Trivia

The trivia-API is gaming project. In this project, users can take quiz. And questions in this quiz could be asked in different fields or in certain field such as Geography, history, sports, art etc.
in addition, there are other facilities such as:

1. view questions: the users can view question all questions or select specific category 
2. add new question: the user can add new question with answer and select its category beside difficulty.
3. search for questions: according to certain query
4. delete question by select button trash


the main objective of this project is structuring plan, implementing, and testing an API. so the system can handle request from client to server, queries the database, format response and status code. also test API endpoint by Curl.


## Starting and Setup

At the beginning the developer need to install different dependencies such as pip, python3, npm.

We have 2 parts of Dependencies here : 1. `Frontend Dependencies`, 2. `Backend Dependencies`

### Frontend Dependencies

In the frontend the react is used as framework. For run frontend should first ```install npm``` dependency.

### Backend Dependencies

After setup and run virtual environment, navigate to the /backend directory and Install all dependencies which found in ```requirement.txt``` by run:

```bash
pip install -r requirements.txt
```


## Running System 
We have three type of running:

1.	running the Frontend
2.	running the server
3.	running the test 


### running the Frontend 

running app by use ```npm start```. After that, the http://localhost:3000 is view 
the running frontend will not view question or anything until we are running the backend


### running the server by execute 
The backend run by :
```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
*note* in windows using `set` rather than `export`

### running the test 

To run test run the following :

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
*note* `createdb` and `dropdb` doesn't work on Windows directly .So rather than using `CREATE DATABASE`, and `DROP database` in `psql `command. Also this command `psql trivia_test < trivia.psql` in windows should specific owner like this  `psql -U postgres trivia < trivia.psql`

## API Reference

### Endpoint

We have different endpoints in this project I will mention some of them  according to difference of method starting with `GET` to `POST` beside `DELETE`

#### GET /categories





