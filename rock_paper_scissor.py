import random
class rock_paper_scissor:
    
    def play_rock_paper_scissors():

        chooser = ["rock", "paper", "scissors"]
        computerChoice = random.choice(chooser) #Prints a random number between 3 and 7
        print("The system generated a random chioce")

        userChoice = int(input("Now it is your turn, enter the number you want \n1. Rock\n2. Paper\n3.Scissors\n"))

        if userChoice == 1:
            userChoice = "rock"
        elif(userChoice == 2):
            userChoice = "paper"
        elif(userChoice == 3):
            userChoice = "scissors"
        else:
            print("NOT ONE OF THE CHOICES!!!")

        if(computerChoice == userChoice):
            print("You both chose " + userChoice + " it's a tie!")
        elif(computerChoice == "rock" and userChoice == "paper"):
            print("Computer: " + computerChoice + " and user: " + userChoice + " user wins!")
        elif(computerChoice == "rock" and userChoice == "scissors"):
            print("Computer: " + computerChoice + " and user: " + userChoice + " comupter wins!")
        elif(computerChoice == "paper" and userChoice == "rock"):
            print("Computer: " + computerChoice + " and user: " + userChoice + " comupter wins!")
        elif(computerChoice == "paper" and userChoice == "scissors"):
            print("Computer: " + computerChoice + " and user: " + userChoice + " user wins!")
        elif(computerChoice == "scissors" and userChoice == "rock"):
            print("Computer: " + computerChoice + " and user: " + userChoice + " user wins!")
        elif(computerChoice == "scissors" and userChoice == "paper"):
            print("Computer: " + computerChoice + " and user: " + userChoice + " comupter wins!")
    play_rock_paper_scissors()
