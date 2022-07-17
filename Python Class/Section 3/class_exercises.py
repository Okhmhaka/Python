# Code to determine if you are high enough to ride the amusement park ride. s

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
age = int(input("What is your age? \n"))
min_height = 120
if height >= min_height:
    print("You are tall enough to ride.\n")
    #age = int(input("What is your age? "))
    if age < 12:
        print("Child Tickets are $5.\n ")
        ticket_price = 5
    elif age <= 18:
        print("Youth Tickets are $7.\n ")
        ticket_price = 7
    else:
        print("Adult Tickets are $12.\n")
        ticket_price = 12
    print("Photos are an additional $3 per ticket.\n ")
    wants_photo = input("Do you want a photo taken? Y or N: \n")
    if wants_photo == "y":
        total = ticket_price + 3
        print(f"The total price of your ticket is {total} ")
    else:
        print(f"The total price of your ticket is {ticket_price} ")
else:
    print("You are not tall enough to ride.")
