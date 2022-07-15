# Simple BMI calculator

weight = input("What is your weight in kilograms (kg)? ")
height = input("What is your height in meters (m)? ")

bmi = round(int(weight) / (float(height) ** 2))
# print(int(bmi))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight. ")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese. ")
