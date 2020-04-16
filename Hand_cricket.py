import sys
import random
wicket = False
out = "No"
numbers = [1, 2, 3, 4, 5, 6]
user_score = 0
computer_score = 0
computer_turn = False
while not wicket and computer_turn is False:
    user_input = int(input("Welcome to hand cricket, please enter a number from 1 to 6\n"))
    if user_input < 1 or user_input > 6:
        sys.exit()
    computer_input = random.choice(numbers)
    print("The computer put: ", computer_input)
    user_score = user_score + user_input
    print("The user's score is: ", user_score)
    if user_input == computer_input:
        print("Out !!!!")
        wicket = True
        computer_turn = True

while out != "Yes":
    print("It's the computers turn to bat")
    user_input = int(input("Input a number from 1 to 6 to make the computer out\n"))
    if user_input < 1 or user_input > 6:
        sys.exit()
    computer_input = random.choice(numbers)
    print("The computer put: ", computer_input)
    computer_score = computer_score + computer_input
    print("The computer's score is: ", computer_score)
    if user_input == computer_input:
        print("Out !!!!")
        out = "Yes"

if user_score > computer_score:
    print("User wins !")
if user_score == computer_score:
    print("It's a tie !!")
else:
    print("Computer wins")