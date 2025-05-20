# Tip Calculator

def get_valid_float(prompt, error_message="Please enter a valid amount."):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("The value can't be negative. Please enter a valid amount.")
            else:
                return value
        except ValueError:
            print(error_message)

def get_valid_choice(prompt, choices, error_message="Please enter a valid choice."):
    while True:
        value = input(prompt).strip()
        if value in choices:
            return value
        else:
            print(error_message)

def get_valid_int(prompt, error_message="Please enter a valid number of people (1, 2, 3, etc.)"):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        else:
            print(error_message)

print("Welcome to the tip calculator.")

# Get the base bill without tip
base_bill = get_valid_float("What was the total bill? > $")

# Get the percentage tip
percentage = get_valid_choice("What percentage tip would you like to give? 10, 12, or 15? > ", ["10", "12", "15"])

# Get the number of people to split the bill
people = get_valid_int("How many people to split the bill? > ")

# Calculate the total bill with tip
total_bill = base_bill * (1 + int(percentage) / 100)

# Calculate the split bill and round to 2 decimal places
split_bill = round(total_bill / people, 2)

# Output the result
print(f"Each person should pay: ${split_bill}")
