from random import randint
import art
import game_data as gd

def play():
    score = 0
    dict_a, index_a = get_entry()
    is_game_over = False

    while not is_game_over:
        dict_b, index_b = get_entry(exclude_one=True, excluded_index=index_a)

        print(art.logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")
        print(f"Compare A: {dict_a['name']}, a {dict_a['description']} from {dict_a['country']}.")
        print(art.vs)
        print(f"Against B: {dict_b['name']}, a {dict_b['description']} from {dict_b['country']}.")
        print('\nWho has more followers? Type "A" or "B":')

        choice = get_input(["A", "B"])

        a_followers = dict_a["follower_count"]
        b_followers = dict_b["follower_count"]

        if a_followers == b_followers or (a_followers > b_followers and choice == "A") or (b_followers > a_followers and choice == "B"):
            score += 1
            dict_a, index_a = dict_b, index_b
            print("\n" * 100)
        else:
            is_game_over = True

    print(art.logo)
    print(f"Sorry that's wrong. Final score: {score}.\n")


def get_entry(exclude_one=False, excluded_index=0):
    entries = len(gd.data)
    while True:
        index = randint(0, entries - 1)
        if not exclude_one or index != excluded_index:
            return gd.data[index], index


def get_input(valid_choices):
    while True:
        choice = input("> ").upper()
        if choice in valid_choices:
            return choice
        formatted = ' or '.join(f'"{c}"' for c in valid_choices)
        print(f"Invalid choice. Please type {formatted}.")


while True:
    play()
    print('Do you want to play another round? Type "Y" or "N":')
    if get_input(["Y", "N"]) == "N":
        break
    print("\n" * 100)

print("Thanks for playing.")
