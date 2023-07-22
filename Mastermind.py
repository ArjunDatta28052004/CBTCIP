# importing required library to choose a random number by the computer
import random

# the computer will choose a random number 
computer = random.randrange(1000, 10000)

#  input from player 1
player1 = int(input("Player 1 please try to guess the 4 digit number: "))

# initialize the number of turns by player1
turns1 = 0

# if the number guessed by player 1 matches the computer in 1st goo then print this
if player1==computer:
    print("Congratulation!!! You have guessed the number in just 1 turns... You are a MasterMind!!!")

# otherwise this
else:

    

    while (player1!=computer):
        turns1 += 1
        # no of digits matched
        count1 = 0

        player1 = str(player1)
        computer = str(computer)

        correct1 = ['_']*4

        # for loop for matching digits
        for i in range(0, 4):
            
            if player1[i]==computer[i]:
                count1 += 1
                correct1[i] = player1[i]

            else:
                continue

        # if the few of the digit(s) matched but not the entire code
        if (count1 < 4) and (count1 != 0):
            print(f"You haven't got the number yet... but seems you have got {count1} digit(s) correctly")
            print(f"These digits are are correct {correct1}")
            print("\n")
        
            player1 = int(input("Try to guess the number again: "))

        # if the digit(s) didn't matched any digit from the number
        if count1==0:
            print("OOOPSS.....There are no digits which are correct in your guess ")
            player1 = int(input("Try to guess the number again: "))

        # when player 1 guessed the number print statement
        if player1 == computer:
            print(f"Congratulations!! You have guessed the number is just {turns1} turns.")
            print("\n")
            print("You are a MasterMind")        


# Same code as above for player 2

computer = random.randrange(1000, 10000)
player2 = int(input("Now Player 2 Please guess the 4 digit number: "))

turns2 = 0
if player2 == computer:
    print("Congratulations!!! You have Guessed the number in just 1 turns. You are a MasterMind")
    
else:

    

    while (player2!=computer):
        turns2 += 1
        count2 = 0

        computer = str(computer)
        player2 = str(player2)

        correct2 = ["_"]*4
        for i in range(0, 4):
            if player2[i]==computer[i]:
                count2 += 1
                correct2[i] = player2[i]
            else:
                continue
            
        if (count2<4) and (count2!=0):
            print(f"You haven't got the number yet... but seems you have {count2} digit(s) correctly")
            print(f"These digits are correct {correct2}")
            print("\n")

            player2 = int(input("Try to guess the number: "))

        if count2 == 0:
            print("OOOPS.... There are no digits correct in your guess")
            player2 = int(input("Try to guess the number: "))

        if player2 == computer:
            print(f"Congratulations..... You have guessed the number in {turns2} turns")
            print("\n")
            print("You are a MasterMind")
            print("\n")

# print statement to declare the winner of the Game 

if turns1<turns2:
    print("CONGRATULATIONS!!!!! PLAYER 1 WINS")

elif turns1==turns2:
    print("IT'S A TIE")

else:
    print("CONGRATULATIONS!!!!! PLAYER 2 WINS")


# NOW LET'S RUN THE CODE