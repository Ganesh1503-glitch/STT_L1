"""Number Guessing Game.

A simple CLI-based game where the user guesses a number between 1 and 100.
"""

import random

def welcome_message():
    """Displays the welcome message and game instructions."""
    print("\nWelcome to the Number Guessing Game!")
    print("guess the number between 1 and 100.\n")

def get_random_number():
    """Returns a random integer between 1 and 100."""
    return random.randint(1, 100)

def get_user_guess():
    """Prompts the user for input and validates it as a number within the correct range."""
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            print("Out of range! Enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def check_guess(guess, secret_number):
    """Checks the user's guess and provides feedback."""
    if guess < secret_number:
        print("Too low! Try again.")
        return False
    if guess > secret_number:
        print("Too high! Try again.")
        return False
    print(f"Congratulations! You guessed the number {secret_number} correctly! 🎉")
    return True

def play_game():
    """Controls the game flow, tracks attempts, and calls necessary functions."""
    secret_number = get_random_number()
    attempts = 0

    while True:
        guess = get_user_guess()
        attempts += 1
        if check_guess(guess, secret_number):
            break

    print(f"You guessed the number in {attempts} attempts.\n")

if __name__ == "__main__":
    welcome_message()
    play_game()
