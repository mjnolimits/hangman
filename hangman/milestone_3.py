# milestone_3.py

import random

# List of favorite fruits
favorite_fruits = ['apple', 'banana', 'orange', 'strawberry', 'kiwi']

# Randomly choose a word from the list
word = random.choice(favorite_fruits)

# Function to check if the guessed letter is in the word
def check_guess(guess):
    guess = guess.lower()
    if guess in word.lower():
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False

# Function to ask the user for input and validate the guess
def ask_for_input():
    while True:
        guess = input("Guess a letter: ")

        # Check if the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            if check_guess(guess):
                break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Call the function to ask for input and check the guess
ask_for_input()
print("The secret word was:", word)
