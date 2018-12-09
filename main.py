import random

list = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

computer = list[random.randint(0, 2)]

print("Welcome to Rock, Paper, Scissors")
print("The rules are simple. Please type 'rock', 'paper', or 'scissors' to play against me! ")
print("The first to reach 5 points wins!")

while player_score < 5 and computer_score < 5:

    player = input ("What do you choose? ")

    if player == computer:
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print ()
            print("You lose and computer gets a point!")
            computer_score += 1
        else:
            print("You win this round and get a point!")
            player_score += 1
    elif player == "paper":
        if computer == "rock":
            print("You win this round and get a point!")
            player_score += 1
        else:
            print("You lose and computer gets a point!")
            computer_score += 1
    elif player == "scissors":
        if computer == "rock":
            print("You lose and computer gets a point!")
            computer_score += 1
        else:
            print("You win and get a point!")
            player_score += 1
    else:
        print("Sorry! Check your spelling!")

    computer = list[random.randint(0, 2)]
print("----------------")
print ("Gameover!")
print ("Your score = " + str(player_score))
print ("Computer score = " + str(computer_score))

if player_score > computer_score:
    print ("You win!")
else:
    print ("You lose!")