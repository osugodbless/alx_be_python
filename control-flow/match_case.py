import random

# Function for guessing game
def play_game():    
    secret_number = random.randint(1, 10)
    guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it? "))

    match guess:
        case number if number == secret_number:
            print("Congratulations, you guessed it!")
        case number if  number > 5 and number <= 10:
            print("Oops, your guess is a bit high. Try again!")
        case number if number > 0 and number <= 5:
            print("Nope, your guess is a bit low. Give it another shot!")
        case _:
            print("Your guess is invalid. Please try again and enter a number between 1 and 10.")

play_game()

# Ask if user wants to play again
play_again = input("Play again? (yes/no)").lower()

if play_again == "yes":
    play_game()
else:
    print("Thank you for playing! Hope to see you again")

