# w0521128_ws5_lists.py
# Creating and Accessing Lists
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Print the first and last items
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Replace the third item with "coconut"
fruits[2] = "coconut"

# Append "fig" to the list
fruits.append("fig")

# Remove "banana" from the list
fruits.remove("banana")

# Print the final list
print("Updated fruit list:", fruits)



#  Traversing Lists

grades = [70, 85, 90, 65, 88]

# Print all grades using a for-each loop
print("\nOriginal Grades:")
for grade in grades:
    print(grade)

# Increase each grade by 5 using an index-based loop
for i in range(len(grades)):
    grades[i] += 5

# Append a new grade 92
grades.append(92)

# Remove the lowest grade
grades.remove(min(grades))

# Print the final list and the average grade
print("\nUpdated Grades:", grades)
average = sum(grades) / len(grades)
print("Average Grade:", average)


