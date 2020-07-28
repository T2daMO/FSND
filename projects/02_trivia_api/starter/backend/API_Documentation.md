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
- Returns: An object with key, question, that contains a object of id(s): answer, category_string,category,difficulty,id,question key:values pairs.
- Sample: curl  http://127.0.0.1:5000/categories
{
	'Success':True,
     'Categories':formated_categories,
     'Total number of categories': len(categories)
     })

```
{
  "question": [
    {
      "answer": "Brazil", 
      "category": "Sports", 
      "category_id": 6, 
      "difficulty": 3, 
      "id": 25, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": "Sports", 
      "category_id": 6, 
      "difficulty": 4, 
      "id": 26, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }
  ], 
  "Success": true, 
  "total_questions": 20
}
}
```

POST '/questions'

- Inserts a dictionary of questions in which the keys are the questions, categories and the value is the corresponding string of the questions and category
- Returns: An object with a single key, questions, that contains a object of id: category_string key:value pairs.
  {
	'Success': true,
	'Total_questions':len(Question.query.all()),
	'questions':questions,
	})

- Sample:curl -X POST http://127.0.0.1:5000/questions --data "{\"question\":\"Whose autobiography is entitled 'I Know Why the Caged Bird Sings'\",\"answer\":\"Maya Angelou\",\"category\":\"4\",\"difficulty\":\"2\",\"type\":\"4\"}" -H "Content-Type: application/json"

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

GET '/questions'
- Fetches a dictionary of questions in which the keys are the questions, categories and the value is the corresponding string of the questions and category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
  {
	'Success': true,
	'Total_questions':len(Question.query.all()),
	'questions':questions,
	})

- Sample: curl -X GET http://127.0.0.1:5000/questions

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

DELETE '/questions/<int:question_id>'

- Deletes contents of a specific question based on an ID
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
  {
	'Success': true,
	'Total_questions':len(Question.query.all()),
	'questions':questions,
	})
- sample: curl -X DELETE http://127.0.0.1:5000/questions/38

```
 "Question": [
    {
      "answer": "Maya Angelou",
      "category": "History",
      "category_id": 4,
      "difficulty": 2,
      "id": 20,
      "question": "Whose autobiography is entitled I Know Why the Caged Bird Sings?"
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
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": "Entertainment",
      "category_id": 5,
      "difficulty": 4,
      "id": 23,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "Entertainment",
      "category_id": 5,
      "difficulty": 3,
      "id": 24,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": "Sports",
      "category_id": 6,
      "difficulty": 3,
      "id": 25,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
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
  ],
  "deleted": 38,
  "success": true,
  "total_questions": 19
}

```