import random
playing = "Yes"
answer = "Yes"
while playing != "No":
    number = random.randint(1, 21)
    guess = int(input("Guess a number from 0 to 20: "))
    if guess == number:
        print("You're correct")
    if guess > number:
        print("The number you guessed is too large")
    if guess < number:
        print("The number you guessed is too small")
    if guess < 1 or guess > 20:
        answer = input("Invalid number, would you like to try again? Yes or No: ")
        if answer == "Yes":
            print("Welcome back")
        else:
            exit()
