import random

# Create a list of 5 favorite fruits
favorite_fruits = ["apple", "banana", "cherry", "date", "elderberry"]
word_list = favorite_fruits

# Use random.choice to select a random word from word_list
word = random.choice(word_list)

def check_guess(guess):
    # Step 2: Convert the guess into lowercase
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in word:
        # If the guess is in the word, print "Good guess!"
        print(f"Good guess! '{guess}' is in the word.")
    else:
        # If the guess is not in the word, print an error message
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input():
    # Step 1: Define a function called ask_for_input
    while True:
        # Step 2: Move the input validation code here
        guess = input("Guess a letter: ")
        if guess.isalpha() and len(guess) == 1:
            # Step 3: Call the check_guess function to check if the guess is in the word
            check_guess(guess)
        else:
            # If the guess doesn't pass the checks, print an error message and continue to prompt for a valid guess
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 4: Call the ask_for_input function to test your code
ask_for_input()
