# importing required libraries
import random 
from random import randint

# initialising the values 
l = ['stone', 'paper', 'scissor', 'Stone', 'Paper', 'Scissor']
player = False
# this line will choose a random value for the computer
computer = l[randint(0,5)]

# main sourse code
while player == False:
    x = input("Enter Stone, Paper, Scissor: ")
    print(f'Your pick is {x} and computer chooses {computer}\n')
    if x == computer:
        print("Tie")
    elif x == "Stone" or x == 'stone':
        if computer == "Scissor" or computer == "scissor":
            print(f"You WIN!!!!! as you choose {x}")
        else:
            print(f"You lost....... as computer chooses {computer}")
    elif x == "Paper" or x == "paper":
        if computer == "Stone" or computer == "stone":
            print(f"You WIN!!!!!! as you choose {x} ")
        else:
            print(f"You lost....... as computer chooses {computer}")
    elif x == "Scissor" or x == "scissor":
        if computer == "Paper" or computer == "paper":
            print(f"You WIN!!!!!! as you choose {x}")
        else:
            print(f"You lost........ as computer chooses {computer}")
    else:
        print("Check spelling mistake\n")
    # whether you want to play it again or not
    
    want_to_play = input("Want to Play again: ")

    if want_to_play == "Yes" or want_to_play == "yes":
        computer = l[randint(0,2)]
        player = False


    else:
        player = True

