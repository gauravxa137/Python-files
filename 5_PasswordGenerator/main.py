import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

print("Welcome to the PyPassword Generator!")

def get_user_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Please enter a valid number.")

# Get user input for the number of each character type
nr_letters = get_user_input("How many letters would you like in your password? > ")
nr_symbols = get_user_input("How many symbols would you like? > ")
nr_numbers = get_user_input("How many numbers would you like? > ")

# Determine password complexity
hard_level = True  # Change this to False for "Easy Level"

# Create a list of characters based on the user's choices
password_characters = (
    random.choices(letters, k=nr_letters) +
    random.choices(symbols, k=nr_symbols) +
    random.choices(numbers, k=nr_numbers)
)

# Shuffle for hard level
if hard_level:
    random.shuffle(password_characters)

# Generate the password
password = ''.join(password_characters)

# Output the result
if password:
    print(f"Here is your password: {password}")
else:
    print("You need to choose at least 1 character to generate a password.")
