# Create a game where you input numbers for either rock, paper, or scissors, and the computer picks a random number to play as it's own.

# Below is the ascii code for rock, paper, and scissors.

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

# Thinking throug this I will need to import random, get an input from the user, utilize if/else statements, and then print out what the user and computer chose.

print("Welcome to the Rock, Paper, Scissors game.")
user_input = input(
    "What is your choice? Type 0 for Rock, 1 for Paper, and 2 for Scissors.")
