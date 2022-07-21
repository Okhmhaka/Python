# This is a small program to randomly generate a heads or tails chance game.

# Import the necessary modules for random
import random

random_integer = random.randint(1, 2)
# print(random_integer)

if random_integer == 1:
    print("The coin landed heads up.")
elif random_integer == 2:
    print("The coin landed tails up.")
