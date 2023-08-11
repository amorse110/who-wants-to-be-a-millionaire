from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

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

    questions = relationship('Question', backref = 'game')

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key = True)
    game_id = Column(Integer, ForeignKey('games.id'))
    content = Column(String)
    category_id = Column(Integer)
    difficulty_id = Column(Integer)

    answers = relationship('Answer', backref = "question")

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

class Difficulty(Base):
    __tablename__ = "difficulties"
    
    id = Column(Integer, primary_key = True)
    level = Column(String)