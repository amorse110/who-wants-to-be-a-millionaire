from helpers import *

if __name__ == '__main__':
    print("Welcome to Who Wants To Be A Millionaire")
    print("Select the game mode you would like to play")

    while True:
        setup_game()
        
        #steps, game setup function (select difficulty, category) use session to select the right questions
        #select some amount randomly to test it
        #helpers need to import