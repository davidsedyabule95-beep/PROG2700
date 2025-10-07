# w0521128_ws5_optional.py
# Nested Lists 

students = [["Alice", 85], ["Bob", 90], ["Charlie", 78]]

# Print each student's name and grade
print("\nStudent Grades:")
for student in students:
    print(student[0], "has grade", student[1])

# Add a new student
students.append(["Diana", 88])

# Increase all grades by 2 points
for student in students:
    student[1] += 2

# Print the updated list
print("\nUpdated Student Grades:")
for student in students:
    print(student[0], "has grade", student[1])
