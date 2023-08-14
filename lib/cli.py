from sqlalchemy.orm import Session
from helpers import setup_game, play_game, session
from db.models import Question

def main():
    print("Welcome to Who Wants to be a Millionaire?")

    while True:
        difficulty, category = setup_game(session)
        if difficulty and category:
            score, total_questions = play_game(session, difficulty, category)

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