#PS 1st Game that is bad because some people don't know how to code properly

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    # I was able to have 11 attempts changing attempts to 1
    attempts = 1
    game_over = False

    while not game_over:

        print(number_to_guess)
        #Type error Converted guess to Integer
        guess = int(input("Enter your guess: "))

        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True

        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True

        elif guess > number_to_guess:
            print("Too high! Try again.")

        elif guess < number_to_guess:
            print("Too low! Try again.")  

        #Attempts are not actually changing added a way to update attempts
        attempts += 1

        #Redundant no need to continue code in loop removed continue
        
    print("Game Over. Thanks for playing!")
start_game()