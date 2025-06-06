import random
name = input("what is your name? ")

#Score of player and computer
player = 0
computer = 0
rounds = int(input("How many rounds do you want to play?(3-10) "))
while rounds < 3 or rounds > 10:
    print("Enter a number between 3 and 10")
    rounds = int(input("How many rounds do you want to play?(3-10) "))

#for and if functions to check if the computer or player wins
for i in range(0, rounds):
    #Ask for user input of rock, papper, or scissors and they them lowercase.
    a = input("What do you choose(rock, papper, or scissors)? ")
    choices = a.lower()
    #Make computer options
    options = ["rock", "papper", "scissors"]
    computer_options = random.choice(options)
    print(computer_options)
    if computer_options == "scissors" and choices == "rock":
        print("Player wins")
        player += 1
    elif computer_options == "rocks" and choices == "papper":
        print("Player wins")
        player += 1
    elif computer_options == "papper" and choices == "scissors":
        print("Player wins")
        player += 1
    elif computer_options == "scissors" and choices == "papper":
        print("Computer wins")
        computer += 1
    elif computer_options == "rocks" and choices == "scissors":
        print("Computer wins")
        computer += 1
    elif computer_options == "papper" and choices == "rock":
        print("Computer wins")
        computer += 1
    elif computer_options == choices:
        print("It is a draw")

    
    
if player > computer:
    print(f"Player {name} won the match")
elif player == computer:
    print("The match draw")
elif player < computer:
    print("Computer won the match")



