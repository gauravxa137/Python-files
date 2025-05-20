# Guess the Number

import random
import art


def play(lower_bound, upper_bound, attempts, cheat_mode):
    """Play a round of the number guessing game."""
    secret_number = random.randint(lower_bound, upper_bound)
    
    if cheat_mode:
        print(f"\n*******************\n"
              f"CHEAT MODE ENABLED:\n"
              f"The number is {secret_number}\n"
              f"*******************\n")
    
    while attempts > 0:
        attempt_text = "attempt" if attempts == 1 else "attempts"
        print(f"You have {attempts} {attempt_text} remaining to guess the number.")
        
        guess = get_integer(lower_bound, upper_bound)
        
        if guess == secret_number:
            print(f"Correct! The number was {secret_number}.\n\nYou win!\n")
            return
        
        print("Too high!" if guess > secret_number else "Too low!")
        attempts -= 1

    print(f"No more attempts left.\nYou lose. The number was {secret_number}.\n")


def choose_difficulty(options):
    """Prompt the user to select a difficulty level and return the number of attempts."""
    choices = list(options.keys())
    prompt = f"Choose a difficulty. Type {', '.join(f'\"{choice}\"' for choice in choices)}:"
    
    while True:
        print(prompt)
        choice = input("> ").lower()
        if choice in options:
            return options[choice]
        print("Invalid option. Please try again.\n")


def get_integer(min_val, max_val):
    """Prompt the user to guess a number within a specific range."""
    while True:
        try:
            guess = int(input("Make a guess:\n> "))
            if min_val <= guess <= max_val:
                return guess
            print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    num_from = -50
    num_to = 50

    difficulties = {
        "easy": 10,
        "hard": 5,
        "extreme": 3,
    }

    testing_mode = False

    while True:
        print(art.logo)
        print("Welcome to the Number Guessing Game!")
        print(f"I'm thinking of a number between {num_from} and {num_to}.")

        attempts = choose_difficulty(difficulties)
        play(num_from, num_to + 1, attempts, testing_mode)

        if input('Enter "y" to play again, or any other key to quit:\n> ').lower() != "y":
            break
        print("\n" * 50)  # Clear screen effect

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
