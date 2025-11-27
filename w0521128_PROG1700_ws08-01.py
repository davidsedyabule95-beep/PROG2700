

print("=" * 70)
print("WORKSHOP 08-01: DATA PROCESSING & REAL-WORLD ANALYSIS LAB")
print("=" * 70)


print("\n  A) WEATHER REPORTER")
print("-" * 70)

temperatures = [14, 16, 18, 17, 20, 19, 15]

print("\nInitial temperature data (°C):")
print(temperatures)

# Calculate initial statistics
total = 0
highest_temp = temperatures[0]
lowest_temp = temperatures[0]
days_above_18 = 0

for temp in temperatures:
    total += temp
    
    if temp > highest_temp:
        highest_temp = temp
    if temp < lowest_temp:
        lowest_temp = temp
    
    if temp > 18:
        days_above_18 += 1

avg = total / len(temperatures)

print(f"\nAverage temperature:    {avg:.2f}°C")
print(f"Highest temperature:    {highest_temp}°C")
print(f"Lowest temperature:     {lowest_temp}°C")
print(f"Days above 18°C:        {days_above_18}")

# Allow user to add more temperatures
print("\nAdd more temperature readings (or type 'done' to finish):")
while True:
    temp_input = input("Enter temperature in °C (or 'done'): ").strip()
    if temp_input.lower() == 'done':
        break
    
    try:
        temp = float(temp_input)
        temperatures.append(temp)
        print(f"✓ Added temperature: {temp}°C")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Remove duplicates using a set
unique_temps = set(temperatures)
print(f"\nUnique temperature readings: {sorted(unique_temps)}")
print(f"Total readings: {len(temperatures)}, Unique: {len(unique_temps)}")

# Recalculate final statistics
total = 0
highest_temp = temperatures[0]
lowest_temp = temperatures[0]
days_above_18 = 0

for temp in temperatures:
    total += temp
    if temp > highest_temp:
        highest_temp = temp
    if temp < lowest_temp:
        lowest_temp = temp
    if temp > 18:
        days_above_18 += 1

avg = total / len(temperatures)

print("\n" + "=" * 70)
print("FINAL WEATHER SUMMARY")
print("=" * 70)
print(f"Total readings:         {len(temperatures)}")
print(f"Average temperature:    {avg:.2f}°C")
print(f"Highest temperature:    {highest_temp}°C")
print(f"Lowest temperature:     {lowest_temp}°C")
print(f"Days above 18°C:        {days_above_18}")


print("\n\n B) LIBRARY CHECKOUT LOG")
print("-" * 70)

books = {
    "Python Basics": 3,
    "Web Design 101": 2,
    "Networking Made Easy": 1
}

print("\nInitial Library Inventory:")
for title, qty in books.items():
    print(f"{title:25} copies: {qty}")

# Interactive checkout/return system
print("\nLibrary Management System")
print("Commands: 'checkout', 'return', or 'done'")

while True:
    action = input("\nEnter command: ").strip().lower()
    
    if action == 'done':
        break
    elif action not in ['checkout', 'return']:
        print("Invalid command. Use 'checkout', 'return', or 'done'.")
        continue
    
    book_title = input("Enter book title: ").strip()
    
    # Add book to inventory if it doesn't exist
    if book_title not in books:
        print(f"'{book_title}' not in system. Adding with 0 copies.")
        books[book_title] = 0
    
    try:
        quantity = int(input(f"Enter quantity to {action}: "))
        
        if action == 'checkout':
            if books[book_title] >= quantity:
                books[book_title] -= quantity
                print(f"✓ Checked out {quantity} copy(ies) of '{book_title}'")
            else:
                print(f"  Warning: Only {books[book_title]} copy(ies) available!")
        
        elif action == 'return':
            books[book_title] += quantity
            print(f"✓ Returned {quantity} copy(ies) of '{book_title}'")
        
        # Prevent negative quantities
        if books[book_title] < 0:
            print("  Warning: Negative quantity detected! Setting to 0.")
            books[book_title] = 0
            
    except ValueError:
        print("Invalid quantity. Please enter a number.")

# Find book with fewest copies
fewest_title = ""
fewest_qty = float('inf')
total_books = 0

for title, qty in books.items():
    total_books += qty
    if qty < fewest_qty:
        fewest_qty = qty
        fewest_title = title

print("\n" + "=" * 70)
print("LIBRARY SUMMARY")
print("=" * 70)
for title, qty in books.items():
    low_stock = "   LOW STOCK" if qty <= 1 else ""
    print(f"{title:30} copies: {qty}{low_stock}")

print(f"\nFewest copies:          {fewest_title} ({fewest_qty})")
print(f"Total books in library: {total_books}")


print("\n\n C) CAMPUS CAFÉ SALES")
print("-" * 70)

items = ["Latte", "Espresso", "Tea", "Muffin"]
sales = [12, 8, 10, 6]

print("\nInitial Sales Report:")
print(f"{'Item':15} {'Sales':>8}")
print("-" * 25)
for i in range(len(items)):
    print(f"{items[i]:15} {sales[i]:>8}")

# Calculate totals and averages
total_sales = 0
best_seller = items[0]
best_sales = sales[0]

for i in range(len(items)):
    total_sales += sales[i]
    if sales[i] > best_sales:
        best_sales = sales[i]
        best_seller = items[i]

avg_sales = total_sales / len(sales)

print(f"\nTotal sales:            {total_sales}")
print(f"Average per item:       {avg_sales:.2f}")
print(f"Best seller:            {best_seller} ({best_sales} sold)")

# Add new items interactively
print("\nAdd new menu items (or type 'done' to finish):")
while True:
    item_name = input("Enter item name (or 'done'): ").strip()
    if item_name.lower() == 'done':
        break
    
    sales_input = input(f"Enter sales count for {item_name}: ").strip()
    try:
        sales_count = int(sales_input)
        if sales_count >= 0:
            items.append(item_name)
            sales.append(sales_count)
            print(f"✓ Added {item_name} with {sales_count} sales")
        else:
            print("Sales count cannot be negative.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Create set of unique items
unique_items = set(items)

# Recalculate final statistics
total_sales = 0
best_seller = items[0]
best_sales = sales[0]

for i in range(len(items)):
    total_sales += sales[i]
    if sales[i] > best_sales:
        best_sales = sales[i]
        best_seller = items[i]

avg_sales = total_sales / len(sales)

print("\n" + "=" * 70)
print("FINAL SALES REPORT")
print("=" * 70)
print(f"{'Item':20} {'Sales':>10}")
print("-" * 32)
for i in range(len(items)):
    star = " " if items[i] == best_seller else ""
    print(f"{items[i]:20} {sales[i]:>10}{star}")

print("-" * 32)
print(f"{'TOTAL':20} {total_sales:>10}")
print(f"\nUnique menu items:      {len(unique_items)}")
print(f"Average sales per item: {avg_sales:.2f}")
print(f"Best-selling item:      {best_seller} ({best_sales} sold)")


print("\n\n🐾 D) PET ADOPTION TRACKER")
print("-" * 70)

adoptions = {
    "Cats": 4,
    "Dogs": 6,
    "Rabbits": 2
}

print("\nInitial Adoption Records:")
for species, count in adoptions.items():
    print(f"{species:10} adopted: {count}")

# Track all unique species in a set
all_species = set(adoptions.keys())

# Allow users to log more adoptions
print("\nLog new adoptions (or type 'done' to finish):")
while True:
    species_name = input("Enter animal type (or 'done'): ").strip()
    if species_name.lower() == 'done':
        break
    
    # Capitalize first letter for consistency
    species_name = species_name.capitalize()
    all_species.add(species_name)
    
    adoption_input = input(f"Enter number of {species_name} adopted: ").strip()
    try:
        adoption_count = int(adoption_input)
        
        if adoption_count < 0:
            print("  Warning: Cannot have negative adoptions!")
            continue
        
        # Add or update adoptions
        if species_name in adoptions:
            adoptions[species_name] += adoption_count
        else:
            adoptions[species_name] = adoption_count
        
        print(f"✓ Logged {adoption_count} {species_name} adoption(s)")
        
    except ValueError:
        print("Invalid input. Please enter a number.")

# Calculate statistics
total_adoptions = 0
most_popular_pet = ""
most_adoptions = 0

for species, count in adoptions.items():
    total_adoptions += count
    if count > most_adoptions:
        most_adoptions = count
        most_popular_pet = species

print("\n" + "=" * 70)
print("ADOPTION SUMMARY REPORT")
print("=" * 70)
print(f"{'Species':15} {'Adoptions':>12} {'Percentage':>12}")
print("-" * 42)

for species, count in sorted(adoptions.items()):
    percentage = (count / total_adoptions * 100) if total_adoptions > 0 else 0
    popular = " " if species == most_popular_pet else ""
    print(f"{species:15} {count:>12} {percentage:>11.1f}%{popular}")

print("-" * 42)
print(f"{'TOTAL':15} {total_adoptions:>12}")

print(f"\nUnique species seen:    {len(all_species)}")
print(f"Most popular pet:       {most_popular_pet} ({most_adoptions} adoptions)")
print(f"All species tracked:    {', '.join(sorted(all_species))}")



# Reflection:

# 1. The Weather Reporter was easiest because it used simple numbers and basic math. No complex stuff.

# 2. Loops help us do the same task many times quickly, saving time when working with lots of data.

# 3. Dictionaries were most useful because they let me connect related things, like names and counts, easily.

# 4. Next, I would add saving data to a file so I don’t lose it and maybe make simple charts to show the data better.