# Step 1

import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
# print word to ensure choice is made correctly (i.e. from list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ")
# Print the letter to ensure correctness
print(guess)

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for char in range(1, guess)
