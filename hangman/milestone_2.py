import random

favorite_fruits = ['apple', 'banana', 'orange', 'strawberry', 'kiwi']
word = random.choice(favorite_fruits)
guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")

else:
    print("Oops! That is not a valid input.")

print("Randomly chosen word:", word)