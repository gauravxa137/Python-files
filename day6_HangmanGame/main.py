import random
import hangman_art as art
import hangman_words as words

def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print(f"You have already guessed the letter \"{guess}\".")
        elif len(guess) != 1 or not guess.isalpha():
            print("The guess has to be a single letter. Please try again.")
        else:
            return guess

def display_word(chosen_word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in chosen_word])

# Initialize game variables
chosen_word = random.choice(words.word_list)
guessed_letters = set()
lives = len(art.stages) - 1

print(art.logo)
print(f"Pssst, the solution is \"{''.join(chosen_word)}\".")  # Remove this line for actual gameplay

# Main game loop
while lives > 0:
    print(display_word(chosen_word, guessed_letters))
    guess = get_guess(guessed_letters)
    guessed_letters.add(guess)

    if guess in chosen_word:
        if all(letter in guessed_letters for letter in chosen_word):
            print(display_word(chosen_word, guessed_letters))
            print("You win!")
            break
    else:
        lives -= 1
        print(f"The letter \"{guess}\" is not in the word. You lose a life.")
        print(art.stages[lives])

if lives == 0:
    print(f"Game over. The word was \"{''.join(chosen_word)}\".")
