import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# This takes the input of names, counts them, and subtracts one to ensure the number counting starts at zero and not one.
random_index = random.randint(0, len(names) - 1)

# Random name generator takes the random integer above and places it in the list brackets as the random number to pull the name in the position
random_name = names[random_index]

# Print the random name to see who buys today.
print(f"{random_name} is going to buy the meal today!")
