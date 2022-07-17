# This exercise is to build an automatic pizza ordering program
# Ask the user what size pizza they want
# Ask the user if they want pepperoni
# Ask the user if they want extra cheese
# Caluclate the total bill based on the user inputs

size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N: \n")
extra_cheese = input("Do you want extra cheese? Y or N: \n")

################################################################
# My Code solution                                             # ################################################################
if size == "S":
    if add_pepperoni == "Y":
        pizza_cost = 17
    else:
        pizza_cost = 15
elif size == "M":
    if add_pepperoni == "Y":
        pizza_cost = 23
    else:
        pizza_cost = 20
else:
    if add_pepperoni == "Y":
        pizza_cost = 28
    else:
        pizza_cost = 25
if extra_cheese == "Y":
    pizza_cost += 1


print(f"Your final bill is: ${pizza_cost}")

################################################################
# Instructor solution to the problem                           #
################################################################

# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is ${bill}")
