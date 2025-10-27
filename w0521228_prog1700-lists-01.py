
movies = ["The Lion King", "Inception", "Spider-Man: Into the Spider-Verse", "Coco", "The Matrix"]

print("My movies list:")
print(movies)                       
print("First movie:", movies[0])     
print("Last movie:", movies[-1])     


movies[1] = "Interstellar"          
print("Updated movies list:", movies)
print()  


# Reading & Accessing Data

numbers = [10, 20, 30, 40, 50]
print("Step 2: numbers list:", numbers)
print("3rd number (index 2):", numbers[2])


print("Last 2 numbers (slice):", numbers[-2:])


print("Total count using len():", len(numbers))


print("Numbers with positions:")
for idx, val in enumerate(numbers, start=1):
    print(f"{idx}. {val}")
print()




inventory = ["milk", "bread", "eggs"]
print("Step 3: Starting inventory:", inventory)


inventory.append("butter")
print("After appending 'butter':", inventory)

inventory.append("cheese")
print("After appending 'cheese':", inventory)

inventory.insert(0, "apples")
print("After inserting 'apples' at beginning:", inventory)

if "bread" in inventory:
    idx = inventory.index("bread")
    inventory[idx] = "whole grain bread"
    print("After replacing 'bread' with 'whole grain bread':", inventory)
else:
    print("'bread' not found to replace.")


if "eggs" in inventory:
    inventory.remove("eggs")
    print("After removing 'eggs':", inventory)
else:
    print("'eggs' not found to remove.")


print("Number of items left in inventory:", len(inventory))
print()


#  To-Do List Manager 

tasks = []

def show_menu():
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. Remove Task (by number)")
    print("3. View Tasks")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task added: '{task}'")
    else:
        print("No task entered. Nothing added.")

def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return
    print("Which task number would you like to remove?")
    view_tasks()
    try:
        num_str = input("Enter task number to remove: ").strip()
        num = int(num_str)
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed task: '{removed}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("Current tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

# Main loop for the to-do manager
while True:
    show_menu()
    choice = input("Choose an option (1-4): ").strip()
    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Thanks for using the To-Do List Manager. Goodbye!")
        break      
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")


# Reflection answers

# 1. What is one real-world use of lists you can think of in your life or work?
#    I use lists to keep my homework tasks and due dates organized. For
#    example, a list of assignments for each class helps me know what I need to finish.

# 2. Which list operation (Create, Read, Update, Delete) do you find easiest or hardest, and why?
#    I find Read and Create easiest because printing items and adding
#    new ones is simple. Update can be harder if I don't know the index of the item I want
#    to change, and Delete can be risky if I remove the wrong item by accident.

# 3. How would you explain the concept of indexing to someone new to Python?
#    Indexing means using a number to pick one item from a list. The
#    first item is index 0, the second is index 1, and so on. So movies[0] gives the
#    first movie. Negative indexes start from the end: movies[-1] is the last movie.


