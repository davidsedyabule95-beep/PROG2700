
import time
import random

#  COUNTING & RANGES
print("STEP 1 – COUNTING & RANGES 🔢")

for i in range(1, 6):
    print("Count:", i)
print("Done!\n")

for i in range(2, 12, 2):
    print(f"{i} ⭐" * i)
print("Counted by twos successfully!\n")

#  backward countdown
for i in range(10, 0, -1):
    print("⏳", i)
    time.sleep(0.3)
print("Blastoff! 🚀\n")


#  PATTERN PRINTING PARTY
print("STEP 2 – PATTERN PRINTING PARTY 🎨")

# Basic triangle
for i in range(1, 6):
    print("*" * i)
print()

# Emoji pyramid
for i in range(1, 6):
    print(" " * (6 - i) + "🎈" * (2 * i - 1))
print()

# Diamond using trees
for i in range(1, 6):
    print(" " * (6 - i) + "🌲" * (2 * i - 1))
for i in range(4, 0, -1):
    print(" " * (6 - i) + "🌲" * (2 * i - 1))
print("Forest complete 🌳\n")

#  STUDENT GRADE SUMMARY
print("STEP 3 – STUDENT GRADE SUMMARY 📊")

students = ["Ava", "Noah", "Liam", "Sophia", "Ashley"]
grades = [88, 92, 79, 95, 84]

print("Student Grade Report:")
for i in range(len(students)):
    result = f"{students[i]} → {grades[i]}%"
    if grades[i] >= 90:
        result += " ⭐"
    elif grades[i] < 60:
        result += " ❌"
    print(result)

average = sum(grades) / len(grades)
print(f"\nClass Average: {average:.1f}%")

if average > 85:
    print("Excellent class performance! 🏆\n")
else:
    print("Keep up the great work everyone!\n")

#  CREATIVE CHALLENGE: LOOP YOUR OWN WAY
print("STEP 4 – CREATIVE CHALLENGE 🎲 COIN FLIP SIMULATOR")

heads = 0
tails = 0

for toss in range(10):
    result = random.choice(["Heads", "Tails"])
    print(f"Toss {toss + 1}: {result}")
    time.sleep(0.2)
    if result == "Heads":
        heads += 1
    else:
        tails += 1

print(f"\nHeads: {heads}, Tails: {tails}")
if heads > tails:
    print("Heads win! 🪙")
elif tails > heads:
    print("Tails win! 🪙")
else:
    print("It's a tie! ⚖️")


#  MULTIPLICATION TABLE
print("\nBONUS CHALLENGE – MULTIPLICATION TABLE 🧮")

for row in range(1, 11):
    for col in range(1, 11):
        value = row * col
        # highlight diagonal
        if row == col:
            print(f"[{value:2}]", end=" ")
        else:
            print(f"{value:3}", end=" ")
    print()

#  Reflection answers 

# 1. What pattern or challenge was most fun, and why?
#     I liked the diamond tree pattern! It felt creative and looked cool in the console.

# 2. How does a for loop differ from a while loop?
#     A for loop runs a set number of times, while a while loop repeats until a condition changes.
#
# 3. What real-world problems could you solve using for loops?
#     Things like calculating totals, generating patterns, or looping through lists of data (like grades).

# 4. How did you ensure your loops didn’t run infinitely?
#     I used range() and controlled counters carefully so that every loop has an endpoint.

# 
print("End of For Loop Fiesta – all steps complete!")
