import random
questions = {
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
  ]
}
formated_questions = [question.format() for question in questions]
print(formated_questions)
print(random.shuffle(formated_questions))
def format():
    return {
      'id': id,
      'question': question,
      'answer': answer,
      'category': category,
      'difficulty': difficulty,
      'category_id': category_id
      }