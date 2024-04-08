# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇

height = 0
students_number = 0

for h in student_heights:
    height += h
    students_number += 1


print(round(height / students_number))

