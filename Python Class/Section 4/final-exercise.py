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
user_input = int(input(
    "What is your choice? Type 0 for Rock, 1 for Paper, and 2 for Scissors:\n "))


# Random choice for the computer.
random_integer = random.randint(0, 2)
# Print the random integer just to test it
# print(random_integer)
if user_input > 3 or user_input < 0:
    print("You typed an invalid number.  You lose!")
if user_input == 0:
    if random_integer == 0:
        print(f"You chose rock: \n{rock}")
        print(f"The computer chose rock: \n{rock}")
        print("You both chose Rock.  Tie Game!! ")
    elif random_integer == 1:
        print(f"You chose rock: \n{rock}")
        print(f"The computer chose paper: \n{paper}")
        print("Paper trumps rock, you lose!! ")
    elif random_integer == 2:
        print(f"You chose rock: \n{rock}")
        print(f"The computer chose scissors: \n{scissors}")
        print("Rock beats scissors, you win!!")
elif user_input == 1:
    if random_integer == 0:
        print(f"You chose paper: \n{paper}")
        print(f"The computer chose rock: \n{rock}")
        print("Paper beats rock, you win!!")
    elif random_integer == 1:
        print(f"You chose paper: \n{paper}")
        print(f"The computer chose paper: \n{paper}")
        print("You both chose paper.  Tie Game!!  ")
    elif random_integer == 2:
        print(f"You chose paper: \n{paper}")
        print(f"The computer chose scissors: \n{scissors}")
        print("Scissors beat paper, you lose!!")
elif user_input == 2:
    if random_integer == 0:
        print(f"You chose scissors: \n{scissors}")
        print(f"The computer chose rock: \n{rock}")
        print("Rock beats scissors, you lose!!")
    elif random_integer == 1:
        print(f"You chose scissors: \n{scissors}")
        print(f"The computer chose paper: \n{paper}")
        print("Scissors beat paper, you win!!")
    elif random_integer == 2:
        print(f"You chose scissors: \n{scissors}")
        print(f"The computer chose scissors: \n{scissors}")
        print("You both chose scissors, tie game!!")
print("Thank you for playing Rock, Paper, Scissors!!")
