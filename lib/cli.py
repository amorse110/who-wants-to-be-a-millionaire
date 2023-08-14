from sqlalchemy.orm import Session
from helpers import setup_game, play_game, session
from db.models import Difficulty, Category

def main():
    print("Welcome to Who Wants to be a Millionaire?")

    while True:
        user, difficulty, category = setup_game(session)
        if difficulty and category:
            difficulty_obj = session.query(Difficulty).filter(Difficulty.level == difficulty).first()
            category_obj = session.query(Category).filter(Category.title == category).first()
            score, total_questions = play_game(session, user, difficulty_obj, category_obj)

            if score == total_questions:
                print("Congratulations, you've won 1 Million Dollars!")
                print("Your final score:", score, "out of", total_questions)
            else:
                print("Game Over. Your final score:", score, "out of", total_questions)

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                break

if __name__ == "__main__":
    main()