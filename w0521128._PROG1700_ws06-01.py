
ticket = ("Halifax", "Toronto", "AC702", 349.99)
print(f"From {ticket[0]} to {ticket[1]} on flight {ticket[2]} costing ${ticket[3]}")

origin, dest, code, price = ticket
print(f"🧳 Traveling from {origin} to {dest} – Flight {code}, ${price}")

flights = [
    ("Halifax", "Montreal", 189.99),
    ("Montreal", "Ottawa", 99.99),
    ("Ottawa", "Toronto", 159.99)
]

for o, d, p in flights:
    print(f"{o} → {d}: ${p}")

print("\nCheap flights:")
for o, d, p in flights:
    if p < 150:
        print(f"{o} → {d}: ${p}")

total = sum(p for _, _, p in flights)
avg = total / len(flights)
print(f"Total: ${total}, Average: ${avg:.2f}")

flight = ("Halifax", "Toronto", 349.99)
print("Before:", flight)
flight = (flight[0], "Vancouver", flight[2] + 150)
print("After:", flight)

def update_flight(f, new_dest, new_price):
    return (f[0], new_dest, new_price)

print(update_flight(flight, "Calgary", 299.99))


orders = [
    ("Alex", "Large", ["Pepperoni", "Mushroom"]),
    ("Priya", "Medium", ["Cheese"]),
    ("Jordan", "Small", ["Veggie", "Onion"])
]

for name, size, toppings in orders:
    print(f"{name} ordered a {size} pizza with {', '.join(toppings)}.")


large_count = sum(1 for _, size, _ in orders if size == "Large")
print("Large pizzas ordered:", large_count)

unique_toppings = {t for _, _, tops in orders for t in tops}
print("All toppings:", unique_toppings)

# Reflection:
# 1. Tuples are useful for storing fixed data that shouldn’t change.
# 2. Step 3 made me think differently since I had to recreate data.
# 3. I enjoyed Step 4 the most—it felt practical and fun.
# 4. Tuples make sense for database rows or coordinates that stay constant.
