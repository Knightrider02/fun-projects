import random
playing = "Yes"
game_list = ("rock", "paper", "scissors")
while playing != "No":
    user_input = input("rock, paper or scissors ")
    computer_input = random.choice(game_list)
    print(computer_input)
    if user_input == computer_input:
        print("It's  a tie")
    if user_input == "rock" and computer_input == "paper":
        print("Computer wins")
    if user_input == "paper" and computer_input == "rock":
        print("User wins")
    if user_input == "rock" and computer_input == "scissors":
        print("User wins")
    if user_input == "scissors" and computer_input == "rock":
        print("Computer wins")
    if user_input == "scissors" and computer_input == "paper":
        print("User wins")
    if user_input == "paper" and computer_input == "scissors":
        print("Computer wins")
    playing = input("Do you want to continue playing, Yes or No ")
