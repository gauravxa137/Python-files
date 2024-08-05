import os
import art

print(art.logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_over = False

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

while not bidding_over:
    print("What's your name?")
    while True:
        name = input("> ")
        if name == "":
            print("Please enter a name.")
        elif name in bids:
            print(f"There is already a bid by {name}. If you want to update your bid, please do so.")
            break
        else:
            break

    print("What is your bid?")
    while True:
        bid_str = input("> $")
        if bid_str == "0":
            print("$0 is not a proper bid. Please try again.")
        elif not bid_str.isdigit():
            print("Please enter a valid amount.")
        else:
            bid = int(bid_str)
            break

    # Update or add the bid
    bids[name] = bid

    print("Are there any other bidders? Type \"yes\" or \"no\".")
    choice = input("> ").lower()
    if choice == "no":
        bidding_over = True

    clear_screen()

# Find the highest bid
winner_name = ""
top_bid = 0
for key, value in bids.items():
    if value > top_bid:
        top_bid = value
        winner_name = key

print(f"The winner is {winner_name} with a bid of ${top_bid}.")
