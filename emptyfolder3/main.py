from rock_paper_scissor.rock_paper_scissor import play_rock_paper_scissors
from number_guessing_game.number_guessing_game import play_number_guessing_game


if __name__ == '__main__':
    game_finished = False
    while not(game_finished):
        print("Welcome! Choose your game:")
        print("[1]: Rock Paper Scissor")
        print("[2]: Number Guessing")
        print("[3]: Exit")
        current_choice = int(input())
        if current_choice == 1:
            play_rock_paper_scissors()
            print("Game over...")
        if current_choice == 2:
            play_number_guessing_game()
            print("Game over...")
        elif current_choice == 3:
            game_finished = True
            print("Thanks for playing!")