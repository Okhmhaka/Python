# Simple BMI calculator

weight = input("What is your weight in kilograms (kg)? ")
height = input("What is your height in meters (m)? ")

bmi = int(weight) / (float(height) ** 2)
print(int(bmi))
