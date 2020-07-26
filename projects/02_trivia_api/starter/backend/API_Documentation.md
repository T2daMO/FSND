# API Reference

##### GETING STARTED
- Base URL: At present this app can only be run locally and is not hosted as a base URL. the backend app is hosted at the default,  http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration
- Authentication: There is currently no authentication or API keys required for this app 

##### Error Handling

errors are returned as JSON objects in the following format:

```
{
	'Success':False,
	'Error':404,
	'Message':"Resource not found!"
},404
```


The API will return four error types when requests fail:

- 400: Bad request
- 404: Resource not found
- 405: Method not allowed
- 422: Unprocessable entity

##### Endpoints

- General
    - Returns a list of Question objects, success value and total number of questions
    - Results are paginated in groups of 10. Include a request argument to chose a page, starting from 1.
    
- Sample: curl  http://127.0.0.1:5000/questions

GET '/questions'
- Fetches a dictionary of questions in which the keys are the questions, categories and the value is the corresponding string of the questions and category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
  {
	'Success': true,
	'Total_questions':len(Question.query.all()),
	'questions':questions,
	})

- Sample:

```
{
  "Success": true,
  "Total_questions": 20,
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": "History",
      "category_id": 4,
      "difficulty": 2,
      "id": 20,
      "question": "Whose autobiography is entitled I Know Why the Caged Bird Sin
    },
    {
      "answer": "Muhammad Ali",
      "category": "History",
      "category_id": 4,
      "difficulty": 1,
      "id": 21,
      "question": "What boxers original name is Cassius Clay?"
    },
    {
      "answer": "Apollo 13",
      "category": "Entertainment",
      "category_id": 5,
      "difficulty": 4,
      "id": 22,
      "question": "What movie earned Tom Hanks his third straight Oscar nominati
    },
    {
      "answer": "Tom Cruise",
      "category": "Entertainment",
      "category_id": 5,
      "difficulty": 4,
      "id": 23,
      "question": "What actor did author Anne Rice first denounce, then praise i
    },
    {
      "answer": "Edward Scissorhands",
      "category": "Entertainment",
      "category_id": 5,
      "difficulty": 3,
      "id": 24,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton
    },
    {
      "answer": "Brazil",
      "category": "Sports",
      "category_id": 6,
      "difficulty": 3,
      "id": 25,
      "question": "Which is the only team to play in every soccer World Cup tour
    },
    {
      "answer": "Uruguay",
      "category": "Sports",
      "category_id": 6,
      "difficulty": 4,
      "id": 26,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": "History",
      "category_id": 4,
      "difficulty": 2,
      "id": 27,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": "Geography",
      "category_id": 3,
      "difficulty": 2,
      "id": 28,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": "Geography",
      "category_id": 3,
      "difficulty": 3,
      "id": 29,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ]
}

```
GET '/categories'

Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.
- Sample: curl  http://127.0.0.1:5000/categories

```
{
	'1' : "Science",
	'2' : "Art",
	'3' : "Geography",
	'4' : "History",
	'5' : "Entertainment",
	'6' : "Sports"
	}
```
Endpoints
GET '/categories'
GET ...
POST ...

POST '/questions'

- Fetches a dictionary of questions in which the keys are the questions, categories and the value is the corresponding string of the questions and category
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
 	





POST '/questions/quiz'
- Fetches questions to play the quiz. 
- Request ArgumentsThis endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```