
# Tuple Basics: Airline Ticket

ticket = ("Halifax", "Toronto", "AC702", 349.99)
print("Step 1 – Airline Ticket Example:")
print("Flight:", ticket)
print(f"From {ticket[0]} to {ticket[1]} on flight {ticket[2]} costing ${ticket[3]}")


origin, destination, flight_no, price = ticket
print(f"✈️  Flying from {origin} to {destination} on flight {flight_no}, costing ${price}! 🧳🌎")
print()  

#  Tuple Collections: Travel Itinerary

flights = [
    ("Halifax", "Montreal", 189.99),
    ("Montreal", "Ottawa", 99.99),
    ("Ottawa", "Toronto", 159.99)
]

print("Step 2 – Travel Itinerary:")
for origin, destination, cost in flights:
    print(f"{origin} → {destination}: ${cost}")

print("\nFlights cheaper than $150:")
for f in flights:
    if f[2] < 150:
        print(f"{f[0]} → {f[1]} (${f[2]})")


total = 0
count = 0
i = 0
while i < len(flights):
    total += flights[i][2]
    count += 1
    i += 1
average = total / count
print(f"\nTotal cost of all flights: ${total:.2f}")
print(f"Average flight cost: ${average:.2f}")
print()


# (Immutability in Action)

flight = ("Halifax", "Toronto", 349.99)
print("Step 3 – Simulating Updates:")
print("Before:", flight)


flight = (flight[0], "Vancouver", flight[2] + 150)
print("After:", flight)

def update_flight(f, new_dest, new_price):
    """Return a new flight tuple with updated destination and price."""
    return (f[0], new_dest, new_price)

print("\nUsing update_flight function:")
updated = update_flight(("Halifax", "Ottawa", 199.99), "Calgary", 299.99)
print("Before:", ("Halifax", "Ottawa", 199.99))
print("After:", updated)


print("\nOptional: Interactive flight updates (enter 'stop' to end):")
sample = ("Halifax", "Toronto", 349.99)
while True:
    dest = input("Enter a new destination or 'stop' to end: ").strip()
    if dest.lower() == "stop":
        break
    try:
        new_price = float(input("Enter new price: "))
        sample = update_flight(sample, dest, new_price)
        print("Updated flight:", sample)
    except ValueError:
        print("Please enter a valid price.")
print()

#  Real-World Mini Challenge: Pizza Orders

orders = [
    ("Alex", "Large", ["Pepperoni", "Mushroom"]),
    ("Priya", "Medium", ["Cheese"]),
    ("Jordan", "Small", ["Veggie", "Onion"])
]

print("Step 4 – Pizza Orders Summary:")
for name, size, toppings in orders:
    toppings_list = " & ".join(toppings)
    print(f"{name} ordered a {size} pizza with {toppings_list}.")

large_count = sum(1 for o in orders if o[1] == "Large")
print(f"\nNumber of Large pizzas ordered: {large_count}")


all_toppings = set()
for _, _, toppings in orders:
    all_toppings.update(toppings)

print("Unique toppings ordered:", all_toppings)
print()


# Reflection answers 

# Reflection:
# 1. Why are tuples useful if you can’t modify them?
#    Tuples are useful for data that shouldn’t change, like flight details or student records.
#    They keep your program predictable and protect data from being accidentally changed.

# 2. In which step did immutability cause you to think differently?
#    In Step 3, because instead of editing a tuple directly, I had to create a new one each time.
#    It made me realize tuples are like “read-only” containers.

# 3. Which exercise did you enjoy most, and why?
#    I liked the pizza orders part because it felt like a real-world task and I got to use lists inside tuples.

# 4. Give one example in real life where tuples make sense.
#    GPS coordinates or student info (name, ID, program) are perfect for tuples since they rarely change.