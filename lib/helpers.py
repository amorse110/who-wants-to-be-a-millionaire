from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ipdb

from db.models import Game, Question, Answer, Category, Difficulty, Base

engine = create_engine('sqlite:///db/game_database.db')
Session = sessionmaker(bind = engine)
session = Session()

def setup_game():
    print("Enter your name")

    print("Choose a difficulty")
    print("A-Easy")
    print("B-Medium")
    print("C-Hard")
    difficulty_choice = input("Enter a letter to choose")
    print("Choose a Category")
    print("A-Animals")
    print("B-History")
    print("C-Science")
    category_choice = input("Enter a letter to choose")
    difficulty_level = ""
    if difficulty_choice == "A":
        difficulty_level = "easy"
    elif difficulty_choice == "B":
        difficulty_level == "medium"
    else:
        difficulty_level == "hard"
    difficulty = session.query(Difficulty).filter(Difficulty.level == difficulty_level).first()
    category = session.query(Category).filter(Category.title)
    [question for question in difficulty.questions if question.category_id == category.id]
    ipdb.set_trace()


    #current_game = game
    #Game(id:2, user:Tom)

    #selected_questions=[Q3, Q4, Q8]
    
    #for question in selected_questions:
        #new_game_question = GameQuestion(game_id=game.id, question_id=question.id)
        #session.add(new_game_question)
        #session.commit()

    #def display_next_question(questions_list):
        #answers = question.answers
        #[0, 1, 2, 3]
        # A  B  C  D    
        #if answers[0][correct_bool]:
            #print("Correct")
        #else
    
    #global current_game
    #current_game.score += 10

    #question = random.choice(question_list)


    # display_random_question(selected_questions)



    