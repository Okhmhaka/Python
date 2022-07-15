# Code to determine if you are high enough to ride the amusement park ride. s

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
min_height = 120
if height >= min_height:
    print("You are tall enough to ride.")
    #age = int(input("What is your age? "))
    if age < 12:
        print("The cost of admission is $5. ")
    elif age <= 18:
        print("The cost of admission is $7. ")
    else:
        print("The cost of admission is $12")
else:
    print("You are not tall enough to ride.")
