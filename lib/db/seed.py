from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game, Question, Answer, Category, Difficulty, Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///game_database.db')
    Base.metadata.create_all (engine)

    Session = sessionmaker(bind = engine)
    session = Session()

    session.query(Game).delete()
    session.query(Question).delete()
    session.query(Answer).delete()
    session.query(Category).delete()
    session.query(Difficulty).delete()
    session.commit()

    question_data = [
        "What are baby kangaroos called?", "What is a female Elephant called",
        "How many toes does a guinea pig have?"
    ]

    question_categories = ["animals", "science", "history"]

