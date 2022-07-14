# With this program we will get inputs for variables a and b, and then switch the variables stored.

# Gather inputs:
from calendar import c


a = input("a: ")
b = input("b: ")

# Do the switch:
c = a
a = b
b = c

# Print the changes:
print("a: " + a)
print("b: " + b)
