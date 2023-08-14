from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key = True)
    running_score = Column(Integer)
    user = Column(String)
    fifty_fifty = Column(Boolean)
    new_question = Column(Boolean)
    extra_time = Column(Boolean)
    double_dip = Column(Boolean)

    game_questions = relationship('GameQuestion', back_populates = 'game')
    questions = association_proxy("game_questions", "question")

class GameQuestion(Base):
    __tablename__ = "game_questions"

    id = Column(Integer, primary_key = True)
    game_id = Column(Integer, ForeignKey('games.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))

    game = relationship('Game', back_populates = 'game_questions')
    question = relationship('Question', back_populates = 'game_questions')

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key = True)
    content = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    difficulty_id = Column(Integer, ForeignKey('difficulties.id'))

    answers = relationship('Answer', backref = "question")
    game_questions = relationship('GameQuestion', back_populates = 'question')

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key = True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    content = Column(String)
    correct_bool = Column(Boolean)

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key = True)
    title = Column(String)

    questions = relationship('Question', backref = 'category')

class Difficulty(Base):
    __tablename__ = "difficulties"
    
    id = Column(Integer, primary_key = True)
    level = Column(String)
    
    questions = relationship('Question', backref = 'difficulty')