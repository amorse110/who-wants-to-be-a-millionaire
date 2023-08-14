from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game, Question, Answer, Category, Difficulty, Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///game_database.db')
    Session = sessionmaker(bind = engine)
    session = Session()

    session.query(Game).delete()
    session.query(Question).delete()
    session.query(Answer).delete()
    session.query(Category).delete()
    session.query(Difficulty).delete()
    session.commit()

    difficulty_easy = Difficulty(level = "easy")
    difficulty_medium = Difficulty(level = "medium")
    difficulty_hard = Difficulty(level = "hard")

    session.add_all([difficulty_easy, difficulty_medium, difficulty_hard])
    session.commit()

    category_animals = Category(title = "animals")
    category_history = Category(title = "history")
    category_science = Category(title = "science")

    session.add_all([category_animals, category_history, category_science])
    session.commit()
    #ANIMALS
    q1 = Question(content="What are baby kangaroos called?", category_id=category_animals.id, difficulty_id = difficulty_easy.id)
    q2 = Question(content="What is the largest species of penguin?", category_id=category_animals.id, difficulty_id = difficulty_easy.id)
    q3 = Question(content="How many legs does a spider typically have?", category_id=category_animals.id, difficulty_id = difficulty_easy.id)

    q4 = Question(content="What are female Elephants called?", category_id=category_animals.id, difficulty_id = difficulty_medium.id)
    q5 = Question(content="Which species of sea turtle is the largest and can be found in oceans around the world?", category_id=category_animals.id, difficulty_id = difficulty_medium.id)
    q6 = Question(content="What is the primary diet of a giant panda?", category_id=category_animals.id, difficulty_id = difficulty_medium.id)

    q7 = Question(content="How many toes does a guinea pig have?", category_id=category_animals.id, difficulty_id = difficulty_hard.id)
    q8 = Question(content="Which creature is often referred to as a living fossil, is a species of fish with a prehistoric appearance, and is known for its bony plates?", category_id=category_animals.id, difficulty_id = difficulty_hard.id)
    q9 = Question(content="What animal is a relative of the manatee and is sometimes referred to as the sea cow?", category_id=category_animals.id, difficulty_id = difficulty_hard.id)
    #HISTORY
    q10 = Question(content="Who was the first President of the United States?", category_id=category_history.id, difficulty_id = difficulty_easy.id)
    q11 = Question(content="Which ancient civilization built the pyramids?", category_id=category_history.id, difficulty_id = difficulty_easy.id)
    q12 = Question(content="What event marked the start of World War I?", category_id=category_history.id, difficulty_id = difficulty_easy.id)

    q13 = Question(content="Which war is often referred to as the Great War?", category_id=category_history.id, difficulty_id = difficulty_medium.id)
    q14 = Question(content="Who was the legendary ruler of the Mongol Empire who conquered a large portion of Asia and Europe?", category_id=category_history.id, difficulty_id = difficulty_medium.id)
    q15 = Question(content="The Industrial Revolution began in which country?", category_id=category_history.id, difficulty_id = difficulty_medium.id)

    q16 = Question(content="Which ancient civilization is credited with developing the world's first known writing system, cuneiform?", category_id=category_history.id, difficulty_id = difficulty_hard.id)
    q17 = Question(content="The Magna Carta, a historical document that limited the power of the monarchy, was signed in which year?", category_id=category_history.id, difficulty_id = difficulty_hard.id)
    q18 = Question(content="The Renaissance began in which European city?", category_id=category_history.id, difficulty_id = difficulty_hard.id)
    #SCIENCE
    q19 = Question(content="What is the primary gas that makes up Earth's atmosphere?", category_id=category_science.id, difficulty_id = difficulty_easy.id)
    q20 = Question(content="What force keeps planets in orbit around the Sun?", category_id=category_science.id, difficulty_id = difficulty_easy.id)
    q21 = Question(content="What is the process by which plants make their own food using sunlight?", category_id=category_science.id, difficulty_id = difficulty_easy.id)

    q22 = Question(content="What is the chemical symbol for gold?", category_id=category_science.id, difficulty_id = difficulty_medium.id)
    q23 = Question(content="What is the main component of Earth's core?", category_id=category_science.id, difficulty_id = difficulty_medium.id)
    q24 = Question(content="Which scientist proposed the theory of general relativity?", category_id=category_science.id, difficulty_id = difficulty_medium.id)

    q25 = Question(content="What is the name of the process by which a solid changes directly into a gas without passing through the liquid state?", category_id=category_science.id, difficulty_id = difficulty_hard.id)
    q26 = Question(content="sample question sh", category_id=category_science.id, difficulty_id = difficulty_hard.id)
    q27 = Question(content="sample question sh", category_id=category_science.id, difficulty_id = difficulty_hard.id)
    
    session.add_all([q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27])
    session.commit()
    
    question_answers = [
        {"question_id" : q1.id, "content" : "Joeys", "correct_bool" : True},
        {"question_id" : q1.id, "content" : "Cubs", "correct_bool" : False},
        {"question_id" : q1.id, "content" : "Kids", "correct_bool" : False},
        {"question_id" : q1.id, "content" : "Phillies", "correct_bool" : False},
        {"question_id" : q2.id, "content" : "Emperor Penguin", "correct_bool" : True},
        {"question_id" : q2.id, "content" : "King Penguin", "correct_bool" : False},
        {"question_id" : q2.id, "content" : "Adélie Penguin", "correct_bool" : False},
        {"question_id" : q2.id, "content" : "Gentoo Penguin", "correct_bool" : False},
        {"question_id" : q3.id, "content" : "12", "correct_bool" : False},
        {"question_id" : q3.id, "content" : "8", "correct_bool" : True},
        {"question_id" : q3.id, "content" : "10", "correct_bool" : False},
        {"question_id" : q3.id, "content" : "6", "correct_bool" : False},
        {"question_id" : q4.id, "content" : "Hens", "correct_bool" : False},
        {"question_id" : q4.id, "content" : "Ladies", "correct_bool" : False},
        {"question_id" : q4.id, "content" : "Cows", "correct_bool" : True},
        {"question_id" : q4.id, "content" : "Queens", "correct_bool" : False},        
        {"question_id" : q5.id, "content" : "Green Turtle", "correct_bool" : False},
        {"question_id" : q5.id, "content" : "Leatherback Turtle", "correct_bool" : True},
        {"question_id" : q5.id, "content" : "Loggerhead Turtle", "correct_bool": False},
        {"question_id" : q5.id, "content" : "Hawksbill Turtle", "correct_bool" : False},
        {"question_id" : q6.id, "content" : "Fish", "correct_bool" : False},
        {"question_id" : q6.id, "content" : "Bamboo", "correct_bool" : True},
        {"question_id" : q6.id, "content" : "Small mammals", "correct_bool" : False},
        {"question_id" : q6.id, "content" : "Grass", "correct_bool" : False},
        {"question_id" : q7.id, "content" : "12", "correct_bool" : False},
        {"question_id" : q7.id, "content" : "14", "correct_bool" : True},
        {"question_id" : q7.id, "content" : "16", "correct_bool" : False},
        {"question_id" : q7.id, "content" : "20", "correct_bool" : False},        
        {"question_id" : q8.id, "content" : "Sturgeon", "correct_bool" : False},
        {"question_id" : q8.id, "content" : "Lungfish", "correct_bool" : False},
        {"question_id" : q8.id, "content" : "Gar", "correct_bool" : False},
        {"question_id" : q8.id, "content" : "Coelacanth", "correct_bool" : True},
        {"question_id" : q9.id, "content" : "Humpback Whale", "correct_bool" : False},
        {"question_id" : q9.id, "content" : "Beluga Whale", "correct_bool" : False},
        {"question_id" : q9.id, "content" : "Narwhal", "correct_bool" : False},
        {"question_id" : q9.id, "content" : "Dugong", "correct_bool" : True},
        {"question_id" : q10.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q10.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q10.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q10.id, "content" : "true answer", "correct_bool" :True},
        {"question_id" : q11.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q11.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q11.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q11.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q12.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q12.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q12.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q12.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q13.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q13.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q13.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q13.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q14.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q14.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q14.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q14.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q15.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q15.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q15.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q15.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q16.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q16.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q16.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q16.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q17.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q17.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q17.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q17.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q18.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q18.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q18.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q18.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q19.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q19.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q19.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q19.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q20.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q20.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q20.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q20.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q21.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q21.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q21.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q21.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q22.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q22.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q22.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q22.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q23.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q23.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q23.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q23.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q24.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q24.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q24.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q24.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q25.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q25.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q25.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q25.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q26.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q26.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q26.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q26.id, "content" : "true answer", "correct_bool" : True},
        {"question_id" : q27.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q27.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q27.id, "content" : "false answer", "correct_bool" : False},
        {"question_id" : q27.id, "content" : "true answer", "correct_bool" : True},
    ]

    for answer in question_answers:
        a = Answer(question_id = answer["question_id"], content = answer["content"], correct_bool = answer["correct_bool"])        
        session.add(a)
        session.commit()