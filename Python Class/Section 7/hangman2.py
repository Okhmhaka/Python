# Step 2
# Import functions and set variables:
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty list called display for the chosen_word
display = []

# A for loop which puts a "_" in each position of the list for the chosen_word
for _ in range(word_length):
    display += "_"

# Insert a while loop so the user can keep guessing. The while loop should stop once all letters have been guessed.
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print(display)

    for position in range(word_length):
        letter = chosen_word[position]
        print(
            f"Current position: {position}\n Current Letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win! Game Over!")
