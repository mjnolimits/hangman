import random

# Create a list of 5 favorite fruits
favorite_fruits = ["apple", "banana", "cherry", "date", "elderberry"]
word_list = favorite_fruits

# Use random.choice to select a random word from word_list
word = random.choice(word_list)

# Step 1: Ask the user to enter a single letter
guess = input("Enter a single letter: ")

# Step 1: Create an if statement to validate the input
if len(guess) == 1 and guess.isalpha():
    # Step 2: If the input is valid, print "Good guess!"
    print("Good guess!")
else:
    # Step 3: If the input is not valid, print "Oops! That is not a valid input."
    print("Oops! That is not a valid input.")