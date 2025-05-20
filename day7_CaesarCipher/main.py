import art

def caesar(cipher_text, shift_amount, cipher_direction):

    # Normalize shift_amount to be within the alphabet length
    if shift_amount > len(alphabet):
        shift_amount %= len(alphabet)

    # Adjust shift amount for decoding
    if cipher_direction == "decode":
        shift_amount = len(alphabet) - shift_amount
    
    text_out = ""
    for char in cipher_text:
        if char in alphabet:
            index_in = alphabet.index(char)
            index_out = index_in + shift_amount
            # Wrap around if the new index is out of range
            if index_out >= len(alphabet):
                index_out -= len(alphabet)
            text_out += alphabet[index_out]
        else:
            # Add non-alphabet characters unchanged
            text_out += char
    
    return text_out

alphabet = 'abcdefghijklmnopqrstuvwxyz'

print(art.logo)

# Repeat unless the user enters "no"
while True:
    print("Type \"encode\" to encrypt, type \"decode\" to decrypt:")
    direction = input("> ").lower()

    while direction not in ["encode", "decode"]:
        print("Invalid choice. Please enter \"encode\" or \"decode\".")
        direction = input("> ").lower()

    print("Type your message:")
    text = input("> ").lower()

    print("Type the shift number:")
    while True:
        shift_str = input("> ")
        if shift_str.isdigit():
            shift = int(shift_str)
            if shift % len(alphabet) == 0:
                print(f"Invalid choice. Shifting by {shift} would result in an identical message.")
            else:
                break
        else:
            print("Invalid choice. Please enter a positive integer.")
    
    result = caesar(cipher_text=text, shift_amount=shift, cipher_direction=direction)
    print(f"The message \"{text}\" {direction}d using a shift of {shift} is \"{result}\".")

    print("Type \"yes\" if you want to go again. Otherwise type \"no\".")
    if input("> ").lower() == "no":
        break

print("Goodbye.")
