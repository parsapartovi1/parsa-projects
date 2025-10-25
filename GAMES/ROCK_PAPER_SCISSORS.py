import random

print("Welcome".center(100 , "-"))

print("Rock Paper Scissors".center(100, "-"))
while True:

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = input("choose rock, paper, or scissors: ").lower()
    print("your choice : " ,player)
    print("computer choice :" ,computer)
    while player not in choices:
        player = int(input("Enter your choice: ")).lower()
    if computer == player:
        print(" ha ha a tie!")

    elif computer == "scissors":
        if player == "rock":
            print("you win")

    elif computer == "rock":
        if player == "scissors":
            print("you lost")

    elif computer == "scissors":
        if player == "paper":
            print("you lost")

    elif computer == "paper":
        if player == "scissors":
            print("you win")

    elif computer == "paper":
        if player == "rock":
            print("you lost")

    elif computer == "rock":
        if player == "paper":
            print("you win !")

    play_again = input("Do you want to play again? (y/n): " ).lower()
    if play_again != "y":
        break
print("written by PARSA")