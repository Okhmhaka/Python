# Tip and bill share calculator
print("Welcome to the tip caclulator!")
total_bill = input("What is the total bill? ")
percent_tip = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")
person_split = input("How many people to split the bill? ")

total_bill = float(total_bill)
percent_tip = float(percent_tip)
person_split = float(person_split)

total_tip = total_bill * (percent_tip/100)
total_bill_tip = total_bill + total_tip
person_pay = round(total_bill_tip / person_split, 2)

print(f"Each person should pay: ${person_pay}")
