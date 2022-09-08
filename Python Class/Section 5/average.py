# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
total_height = 0
count = 0
for height in student_heights:
    total_height = total_height + height
    count = count + 1
average_height = total_height / count
average_height = round(average_height)

print(f"The sum of the student height is {total_height}")
print(f"The total number of students measured is {count}")
print(f"The average student height is {average_height}.")
