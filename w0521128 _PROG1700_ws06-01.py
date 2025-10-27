
# Creating a tuple that stores a customer's record.
customer = ("John Doe", "Premium", "Canada")
print("Step 2 – CREATE")
print("Customer Record:", customer)

# Accessing each item individually using indexing
print("Customer Name:", customer[0])
print("Account Type:", customer[1])
print("Country:", customer[2])
print()  # blank line for spacing


# Accessing tuple data and looping through it.
print("Step 3 – READ")
for field in customer:
    print("Field:", field)
print()


print("Step 4 – UPDATE")
customer = ("John Doe", "Platinum", "Canada")
print("Updated Customer Record:", customer)
print("Note: The tuple was recreated with new data (immutability in action).")
print()


print("Step 5 – DELETE")
del customer
print("Customer tuple deleted successfully.")

print()

# Using tuples to store flight information.
print("Step 6 – REAL-WORLD EXAMPLE")
flight = ("AC123", "Halifax", "Toronto", "10:30 AM")
print(f"Flight {flight[0]} departs from {flight[1]} to {flight[2]} at {flight[3]}")

flight = ("AC123", "Halifax", "Toronto", "12:00 PM")
print("Updated flight record:", flight)
print()


# Reflection answers
# 1. Why can’t tuples be updated directly like lists?
#    Because tuples are immutable. Once created, their data cannot change.
#    This protects important data from being accidentally modified.

# 2. What are some advantages of immutability in programming?
#    It makes programs more predictable, prevents bugs, and helps with secure data handling.

# 3. Give one real-world example where tuples make more sense than lists.
#    Storing fixed data such as GPS coordinates, student records, or flight info
#    — data that should not be changed during program execution.
