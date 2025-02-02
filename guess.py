import random

def welcome_message():
    print("\nWelcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.\n")

def get_random_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Out of range! Enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def check_guess(guess, secret_number):
    if guess < secret_number:
        print("Too low! Try again.")
        return False
    elif guess > secret_number:
        print("Too high! Try again.")
        return False
    else:
        print(f"Congratulations! You guessed the number {secret_number} correctly! 🎉")
        return True

def play_game():
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
