import random

# ASCII art for the choices
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List for easier access
choices_list = [rock, paper, scissors]
options_list = ["0", "1", "2"]

def get_player_choice():
    print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
    while True:
        choice_str = input("> ")
        if choice_str in options_list:
            return int(choice_str)
        else:
            print("Invalid choice. Type 0 for Rock, 1 for Paper, or 2 for Scissors.")

def get_cpu_choice():
    return random.randint(0, 2)

def print_choices(player_choice, cpu_choice):
    print(f"\nYou chose:\n{choices_list[player_choice]}")
    print(f"Computer chose:\n{choices_list[cpu_choice]}")

def determine_winner(player_choice, cpu_choice):
    if player_choice == cpu_choice:
        return "It's a tie."
    elif (player_choice == 0 and cpu_choice == 2) or \
         (player_choice == 1 and cpu_choice == 0) or \
         (player_choice == 2 and cpu_choice == 1):
        return "You win."
    else:
        return "You lose."

def play_game():
    player_choice = get_player_choice()
    cpu_choice = get_cpu_choice()
    print_choices(player_choice, cpu_choice)
    result = determine_winner(player_choice, cpu_choice)
    print(result)

# Start the game
play_game()
