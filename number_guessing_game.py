# guessing game
import random
class number_guessing_game:

    def number_guessing_game():

        randomized = random.randint(0, 51) #Prints a random number between 3 and 7
        print("The system generated a random number between 0 and 50")
        flag = False
        while not flag:
            guess = int(input("try to guess the number: "))

            if randomized == guess:
                flag = True
            elif randomized > guess:
                print("Try a higher number")
            else:
                print("Try a smaller number")
        print("YOU GOT IT! the number is " + str(randomized))

    number_guessing_game()
