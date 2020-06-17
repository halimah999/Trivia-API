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

**In general** return list of categories

**Sample:** `curl http://127.0.0.1:5000/categories`

```bash
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true:
}

```
#### GET /questions

**In general** Returns a list questions, list of categories and total number of questions. And the Results are paginated in groups of 10.

**Sample:** `curl http://127.0.0.1:5000/questions`


```bash
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    }
  ],
  "success": true,
  "total_questions": 34
}
```


#### DELETE /questions/<int:id>

**In general** Return deleted item 

**Sample:**  `curl http://127.0.0.1:5000/questions/6 -X DELETE`
```bash
{
  "Deleted": 9,
  "success": true
}
```
#### POST /questions

**In general**  Return true if inserted success 

**Sample:** `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{ "question": " is this new question?", "answer": "yes", "difficulty": 1, "category": 4}'`

**Sample in windows:** `curl -i -X POST -H "Content-Type: application/json" -d "{\"question\":\"is this new question?\",\"answer\":\"yes\",\"difficulty\":1,\"category\":4}" http://127.0.0.1:5000/questions`
```bash
{
  "success": true
}
```
#### POST /searches

**In general**  return  only questions that include the searchTerm , the list of category for these questions and total of these questions

**Sample in windows:** `curl -i -X POST -H "Content-Type: application/json" -d "{\"searchTerm\":\"what\"}" http://127.0.0.1:5000/searches`

```bash
{
  "current_category": [
    3,
    2,
    1,
    1
  ],
  "questions": [
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "success": true,
  "total_questions": 4
}

```

#### GET categories/<int:id>/questions

**In general**  Return current category and list of questions in this category 

**Sample:** `Curl http://127.0.0.1:5000/categories/4/questions`

```bash
{
  {
  "current_category": 4,
  "questions": [
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
  "success": true,
}

}
```

#### POST /quizzes

**In general**  return each time only one question blong to specified id of catgory and not in  previous questions

**Sample :** `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [12,23],"quiz_category": {"id": 4,"type": "History"}}'`

```bash
{
  "question": {
    "answer": "yes",
    "category": 4,
    "difficulty": 1,
    "id": 71,
    "question": "is this new question?"
  },
  "success": true
}

```


### Error Handling
 erros also returned as json not  html For example as following in bad request:

```bash
{
    "success": False,
    "error": 400,
    "message": "bad request"
}
```


The API will return diffrent types of errors:

1. 400 –> bad request
2. 404 –> resource not found
3. 422 –> unprocessable
4. 500 -> internal server error







