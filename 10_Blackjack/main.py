import random
import art

def draw_card(count):
    """Returns a LIST with 'count' amount of random cards from a standard deck."""
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    drawn_cards = [random.choice(card_deck) for _ in range(count)]
    return drawn_cards

def calculate_score(card_list):
    """Calculates and returns the score for a list of cards."""
    score = sum(card_list)
    # Handle Aces (value 11) which can be 1 if the score exceeds 21
    while score > 21 and 11 in card_list:
        score -= 10
        card_list.remove(11)
    return score

def display_score(plyr_list, game_over):
    """Displays the current score for all players."""
    dealer = plyr_list[0]
    player = plyr_list[1]
    
    if dealer["has_blackjack"]:
        print(f"Dealer's cards: {fix_aces(dealer['cards'])} BLACKJACK!")
    elif game_over:
        print(f"Dealer's cards: {fix_aces(dealer['cards'])} Score: {dealer['score']}")
    else:
        print(f"Dealer's first card: {fix_aces(dealer['revealed_cards'])} Score: ??")

    if player["has_blackjack"]:
        print(f"Your cards: {fix_aces(player['cards'])} BLACKJACK!")
    else:
        print(f"Your cards: {fix_aces(player['cards'])} Score: {player['score']}")

def fix_aces(card_list):
    """Formats the list of cards, changing aces from '11' to 'A'."""
    return "".join(f"[{'A' if val == 11 else val}]" for val in card_list)

def play():
    """Play one round of Blackjack."""
    cpu = {
        "cards": [],
        "revealed_cards": [],
        "score": 0,
        "has_blackjack": False
    }
    user = {
        "cards": [],
        "score": 0,
        "has_blackjack": False
    }
    list_of_players = [cpu, user]

    # Initial dealing
    for player in list_of_players:
        player["cards"] = draw_card(2)
        player["score"] = calculate_score(player["cards"])
        if player["score"] == 21:
            player["has_blackjack"] = True
    
    # Reveal dealer's first card
    cpu["revealed_cards"] = [cpu["cards"][0]]

    # Check for instant win
    if cpu["has_blackjack"] or user["has_blackjack"]:
        display_score(list_of_players, True)
        return

    # User's turn
    while not user["has_blackjack"]:
        display_score(list_of_players, False)
        print("\nType 'y' to get another card, type 'n' to pass.")
        card_choice = input("> ").lower()
        if card_choice == 'y':
            user["cards"].extend(draw_card(1))
            user["score"] = calculate_score(user["cards"])
            if user["score"] > 21:
                break
        else:
            break

    # Dealer's turn
    while cpu["score"] < 17:
        print("The dealer draws a card.\n")
        cpu["cards"].extend(draw_card(1))
        cpu["score"] = calculate_score(cpu["cards"])

    # Game over
    display_score(list_of_players, True)

    # Determine winner
    if cpu["has_blackjack"] and not user["has_blackjack"]:
        print("\nDealer has a blackjack, DEALER wins.\n")
    elif user["has_blackjack"] and cpu["has_blackjack"]:
        print("\nYou both have a blackjack, it's a tie!\n")
    elif user["has_blackjack"]:
        print("\nYou have a blackjack, YOU win.\n")
    elif cpu["score"] > 21:
        print("\nDealer went over. YOU win.\n")
    elif user["score"] > 21:
        print("\nYou went over. DEALER wins.\n")
    elif user["score"] == cpu["score"]:
        print("\nIt's a tie!\n")
    elif user["score"] > cpu["score"]:
        print("\nYOU win.\n")
    else:
        print("\nDEALER wins.\n")

# Main loop
while True:
    print(art.logo)
    play()
    print("Do you want to play another round? (y/n)")
    if input("> ").lower() != 'y':
        break
    print("\n" * 100)

print("Thanks for playing!")
