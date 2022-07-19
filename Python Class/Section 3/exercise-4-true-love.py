# In this exercise I will demonstrate how to use different logical operators
# within a pretend Love Calculator.  The goal is to take two peoples names and
# determine how many letters in their name match the letters in TRUE LOVE.
# Then combine the numbers together to make a two digit number.

# Ask each person what their first and last name are

first_person_name = input("What is your first and last name? \n")
second_person_name = input("Waht is their first and last name? \n")

# ensure the first and last name of each peson is all in lower case:
first_person_name = first_person_name.lower()
second_person_name = second_person_name.lower()

both_names = first_person_name + second_person_name

number_of_t = both_names.count("t")
number_of_r = both_names.count("r")
number_of_u = both_names.count("u")
number_of_e = both_names.count("e")
number_of_l = both_names.count("l")
number_of_o = both_names.count("l")
number_of_v = both_names.count("o")


count_true = int(number_of_t + number_of_r + number_of_u + number_of_e)
count_love = int(number_of_l + number_of_o + number_of_v + number_of_e)

total = int(str(count_true) + str(count_love))

if total <= 10 or total > 90:
    print(f"Your score is {total}, and you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, and you are alright together. ")
else:
    print(f"Your score is {total}")
