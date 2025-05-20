import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return n1 / n2

def list_operations():
    text = "Available operations: " + " ".join(operations.keys())
    print(text)

def get_input(is_symbol=False):
    if is_symbol:
        while True:
            sym = input("> ")
            if sym in operations:
                return sym
            else:
                print(f"{sym} is not a valid option.")
                list_operations()
                print("Please select one of the above.")
    else:
        while True:
            num_string = input("> ")
            if num_string == "":
                print("Please enter a value.")
            elif is_float(num_string):
                return float(num_string)
            else:
                print("Please enter a valid number.")

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

new_calculation = True
result = 0

while True:
    if new_calculation:
        print(art.logo)
        print("What's the first number?")
        num1 = get_input()
    else:
        num1 = result

    list_operations()

    print("Pick an operation from the above line:")
    symbol = get_input(is_symbol=True)

    print("What's the next number?")
    while True:
        num2 = get_input()
        if symbol == "/" and num2 == 0:
            print("You have chosen to divide by zero. Please input a non-zero number.")
        else:
            break

    calculation_result = operations[symbol](num1, num2)
    if calculation_result is not None:
        result = calculation_result
        print(f"{num1} {symbol} {num2} = {result}")

    print(f"Type \"y\" to continue calculating with {result}, or type \"n\" to start a new calculation. "
          f"Anything else will exit the program.")
    choice = input("> ").lower()
    if choice == "y":
        new_calculation = False
    elif choice == "n":
        new_calculation = True
    else:
        break

print("Goodbye.")
