import random
import art

def play(a, b, diff, cheat_mode):
    """Play a round using the provided parameters."""
    secret_num = random.randint(a, b)
    if cheat_mode:
        print(f"\n**********\nCHEAT MODE ENABLED:\nThe number is {secret_num}\n**********\n")
    
    lives = diff
    victory = False
    
    while lives > 0:
        print(f"You have {lives} {'attempts' if lives > 1 else 'attempt'} remaining to guess the number.")
        guess = get_integer(a, b)
        
        if guess == secret_num:
            victory = True
            break
        elif guess > secret_num:
            print("Too high!")
        else:
            print("Too low!")
        
        lives -= 1
    
    print(f"\nThe number was {secret_num}.")
    print("\nYou win!\n" if victory else "\nYou lose.\n")

def choose_difficulty(att_dict):
    """Prompts user to choose a difficulty and returns the corresponding number of attempts."""
    choices_list = [f"\"{key}\"" for key in att_dict]
    print(f"Choose a difficulty. Type {' or '.join(choices_list)}:")
    
    while True:
        diff_choice = input("> ").lower()
        if diff_choice in att_dict:
            return att_dict[diff_choice]
        print(f"Invalid option. Please choose {' or '.join(choices_list)}.")

def get_integer(a, b):
    """Prompts user to input a number within the provided range and returns it."""
    while True:
        try:
            guess_int = int(input("Make a guess:\n> "))
            if a <= guess_int <= b:
                return guess_int
            print(f"Please enter an integer between {a} and {b}.")
        except ValueError:
            print("Please enter a valid integer.")

# Main loop
def main():
    num_from = -50
    num_to = 50
    attempts_dict = {
        "easy": 10,
        "hard": 5,
        "extreme": 3,
    }
    testing_mode = False

    print(art.logo)
    print("Welcome to the Number Guessing Game!\n")
    print(f"I'm thinking of a number between {num_from} and {num_to}.")
    
    while True:
        attempts = choose_difficulty(attempts_dict)
        play(num_from, num_to, attempts, testing_mode)
        
        if input("Enter \"y\" to play again, or anything else to quit.\n> ").lower() != "y":
            break
        print("\n" * 100)
    
    print("Thanks for playing.")

if __name__ == "__main__":
    main()
