# Random Password Generator Project

from math import radians
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# There are two ways to do this.  The easy way and the hard way.  The easy way is no randomization, but to generate letters, numbers, and symbols
# in order.  vE34$%

# Start out by making password an empty string with:
password = ""

# Write a for loop to pull the number of characters from the lists
# This for loop will pick a character withing the letters list based on the number of letters desired from user input.
for char in range(1, nr_letters + 1):
    # the random.choice will let the program pick the random letter withing letters list
    random_char = random.choice(letters)
    password += random_char
# print(password)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

print(password)

# Hard level - Order of characters randomized

# The simplest way is to use the join command with password and create a for loop.

secure_pass = ''.join(random.choice(password) for i in range(len(password)))

print(secure_pass)

##############################################

# The instructor solution is to take the random characters, put then into a list, shuffle the list, then use a for loop to put them back into a string to print.

password_list = []
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

# print(password_list)

# now to randomize the password.

random.shuffle(password_list)

for char in password_list:
    password += char
print(password)
