from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Game, Question, Category, Difficulty, GameQuestion, Base
import random

engine = create_engine('sqlite:///db/game_database.db')
Session = sessionmaker(bind = engine)
session = Session()

def setup_game(session: Session):
    print("Enter your name:")
    user_name = input("Name: ")

    print("Choose a difficulty")
    print("A-Easy")
    print("B-Medium")
    print("C-Hard")
    difficulty_choice = input("Enter a letter to choose-> ")
    
    print("Choose a Category")
    print("A-Animals")
    print("B-History")
    print("C-Science")
    category_choice = input("Enter a letter to choose-> ")
    
    difficulty_level = ""
    if difficulty_choice == "A":
        difficulty_level = "easy"
    elif difficulty_choice == "B":
        difficulty_level = "medium"
    else:
        difficulty_level = "hard"
    
    category_level = ""
    if category_choice == "A":
        category_level = "animals"
    elif category_choice == "B":
        category_level = "history"
    else:
        category_level = "science"
    
    difficulty = session.query(Difficulty).filter(Difficulty.level == difficulty_level).first()
    # print("Retrieved Difficulty:", difficulty)
    
    category = session.query(Category).filter(Category.title == category_level).first()
    # print("Retrieved Category:", category)
    
    return user_name, difficulty.level, category.title
    
def play_game(session, user, difficulty, category):
    questions = (
        session.query(Question)
        .join(Category)
        .join(Difficulty)
        .filter(Difficulty.level == difficulty.level, Category.title == category.title)
        .all()
    )

    new_game = Game(running_score=0, user=user)
    session.add(new_game)
    session.commit()

    total_questions = len(questions)
    score = 0

    for _ in range(total_questions):
        random.shuffle(questions)
        question = questions.pop()

        game_question = GameQuestion(game=new_game, question=question)
        session.add(game_question)
        session.commit()

        print("\nQuestion:", question.content)
        answers = question.answers

        for index, answer in enumerate(answers, start=1):
            print(f"{index}. {answer.content}")

        user_answer = int(input("Enter your answer (1, 2, 3, or 4): ")) - 1

        if answers[user_answer].correct_bool:
            print("Correct!")
            score += 1
            new_game.running_score = score
            session.commit()
        else:
            print("Incorrect! The correct answer was:", [a.content for a in answers if a.correct_bool][0])
            break

    return score, total_questions