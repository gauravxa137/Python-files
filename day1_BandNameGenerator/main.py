# Band Name Generator

print("Welcome to the Band Name Generator.")

def get_user_input(prompt):
    while True:
        print(prompt)
        user_input = input("> ")
        if user_input.strip():
            return user_input
        else:
            print("You haven't entered anything. Please try again.")

# Get the city name and pet name from the user
hometown = get_user_input("What's the name of the city you grew up in?")
pet = get_user_input("What's your pet's name?")

# Output the band name
print(f"Your band name could be {hometown} {pet}.")
