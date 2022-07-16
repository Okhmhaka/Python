# This script is designed to determine whether a given year is a leap year based on current calendar rules

# Get input from user for a given year:

year = int(input("Which year do you want to check? "))

# Calculate the remainders to determine if they are evevnly divisible.
# Using the % will determine if a remainder exists.
# If no remainder exists, then the year is evenly divisible by the given numbers

year_divisible_by_four = year % 4
year_divisible_by_hundred = year % 100
year_divisible_by_four_hundred = year % 400

# Begin the conditional statements to check which year is a leap year.
# Rules for leap years:
#   On every year that is evenly divisible by 4
#   **Except every year that is evenly divisible by 100
#   **Unless the year is also evenly divisible by 400

if year_divisible_by_four == 0:
    if year_divisible_by_hundred != 0:
        print("Leap Year")
    elif year_divisible_by_four_hundred == 0:
        print("Leap Year")
    else:
        print("Not a Leap Year")
else:
    print("Not a Leap Year")
