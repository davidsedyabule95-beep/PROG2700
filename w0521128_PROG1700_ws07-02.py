
print("=" * 60)
print("WORKSHOP 07-02: DATA PROCESSING & INTEGRATION LABS")
print("=" * 60)


print("\n🛒 A) GROCERY ANALYZER")
print("-" * 60)

groceries = {
    "Apples": 3.50,
    "Bananas": 2.75,
    "Bread": 2.99,
    "Milk": 4.29,
    "Eggs": 3.49
}

# Display initial groceries and calculate total
print("\nInitial Grocery List:")
total = 0
most_expensive_item = ""
most_expensive_price = 0

for item, price in groceries.items():
    # Apply 10% discount if price is above $4.00
    if price > 4.00:
        discounted_price = price * 0.9
        print(f"{item:10} ${price:5.2f} → ${discounted_price:5.2f} (10% OFF!)")
        total += discounted_price
    else:
        print(f"{item:10} ${price:5.2f}")
        total += price
    
    # Track most expensive item
    if price > most_expensive_price:
        most_expensive_price = price
        most_expensive_item = item

print(f"\nNumber of items: {len(groceries)}")
print(f"Most expensive item: {most_expensive_item} at ${most_expensive_price:.2f}")
print(f"Total cost: ${total:.2f}")

# Allow user to add more items
print("\nAdd more items (or type 'done' to finish):")
while True:
    item_name = input("Enter item name (or 'done'): ").strip()
    if item_name.lower() == 'done':
        break
    
    price_input = input(f"Enter price for {item_name}: $").strip()
    try:
        price = float(price_input)
        groceries[item_name] = price
        print(f"✓ Added {item_name} at ${price:.2f}")
    except ValueError:
        print("Invalid price. Please enter a number.")

# Recalculate final total
total = 0
for item, price in groceries.items():
    if price > 4.00:
        total += price * 0.9
    else:
        total += price

print(f"\nFinal total cost: ${total:.2f}")


print("\n\n🎓 B) STUDENT TRACKER")
print("-" * 60)

students = ["Ava", "Noah", "Liam"]
grades = [88, 92, 79]

print("\nInitial Student Grades:")
for i in range(len(students)):
    print(f"{students[i]:15} → {grades[i]}")

# Add more students
print("\nAdd more students (or type 'done' to finish):")
while True:
    student_name = input("Enter student name (or 'done'): ").strip()
    if student_name.lower() == 'done':
        break
    
    grade_input = input(f"Enter grade for {student_name}: ").strip()
    try:
        grade = int(grade_input)
        if 0 <= grade <= 100:
            students.append(student_name)
            grades.append(grade)
            print(f"✓ Added {student_name} with grade {grade}")
        else:
            print("Grade must be between 0 and 100.")
    except ValueError:
        print("Invalid grade. Please enter a number.")

# Calculate statistics
total_grades = 0
highest_grade = grades[0]
lowest_grade = grades[0]
honour_roll = set()

for i in range(len(students)):
    total_grades += grades[i]
    
    if grades[i] > highest_grade:
        highest_grade = grades[i]
    if grades[i] < lowest_grade:
        lowest_grade = grades[i]
    
    # Add to honour roll if grade >= 90
    if grades[i] >= 90:
        honour_roll.add(students[i])

average_grade = total_grades / len(grades)

print("\n" + "=" * 60)
print("GRADE STATISTICS")
print("=" * 60)
print(f"Number of students:  {len(students)}")
print(f"Average grade:       {average_grade:.2f}")
print(f"Highest grade:       {highest_grade}")
print(f"Lowest grade:        {lowest_grade}")
print(f"\nHonour Roll (≥90):   {', '.join(honour_roll) if honour_roll else 'None'}")

 
# GAME SCOREBOARD

print("\n\n🏀 C) GAME SCOREBOARD")
print("-" * 60)

scores = {"Alex": 12, "Priya": 18, "Jordan": 9}

print("\nInitial Scores:")
for name, points in scores.items():
    print(f"{name:10} {points} pts")

# Update or add players
print("\nUpdate/Add players (or type 'done' to finish):")
while True:
    player_name = input("Enter player name (or 'done'): ").strip()
    if player_name.lower() == 'done':
        break
    
    score_input = input(f"Enter score for {player_name}: ").strip()
    try:
        score = int(score_input)
        scores[player_name] = score
        
        # Check for level up
        if score > 20:
            print(f"🎉 Level Up! {player_name} has exceeded 20 points!")
        else:
            print(f"✓ Updated {player_name} to {score} pts")
    except ValueError:
        print("Invalid score. Please enter a number.")

# Find top player
top_player = ""
max_score = 0
for name, points in scores.items():
    if points > max_score:
        max_score = points
        top_player = name

print("\n" + "=" * 60)
print("FINAL SCOREBOARD")
print("=" * 60)
for name, points in scores.items():
    leader_marker = " 👑" if name == top_player else ""
    level_marker = " 🔥" if points > 20 else ""
    print(f"{name:10} {points} pts{leader_marker}{level_marker}")

print(f"\n🏆 Top Player: {top_player} with {max_score} points!")


print("\n\n🎶 D) PLAYLIST ANALYZER")
print("-" * 60)

songs = ["Song A", "Song B", "Song C"]
plays = [5, 10, 7]

print("\nInitial Playlist:")
for i in range(len(songs)):
    print(f"{songs[i]:15} {plays[i]} plays")

# Add new songs interactively
print("\nAdd more songs (or type 'done' to finish):")
while True:
    song_name = input("Enter song name (or 'done'): ").strip()
    if song_name.lower() == 'done':
        break
    
    play_input = input(f"Enter play count for {song_name}: ").strip()
    try:
        play_count = int(play_input)
        if play_count >= 0:
            songs.append(song_name)
            plays.append(play_count)
            print(f"✓ Added {song_name} with {play_count} plays")
        else:
            print("Play count must be non-negative.")
    except ValueError:
        print("Invalid play count. Please enter a number.")

# Create set of unique songs (removes duplicates)
unique_songs = set(songs)

# Calculate statistics
total_plays = 0
most_played_song = songs[0]
most_played_count = plays[0]
least_played_song = songs[0]
least_played_count = plays[0]

for i in range(len(songs)):
    total_plays += plays[i]
    
    if plays[i] > most_played_count:
        most_played_count = plays[i]
        most_played_song = songs[i]
    
    if plays[i] < least_played_count:
        least_played_count = plays[i]
        least_played_song = songs[i]

average_plays = total_plays / len(plays)

print("\n" + "=" * 60)
print("PLAYLIST STATISTICS")
print("=" * 60)
print(f"Total songs:         {len(songs)}")
print(f"Unique songs:        {len(unique_songs)}")
print(f"Total plays:         {total_plays}")
print(f"Average plays:       {average_plays:.2f}")
print(f"Most played:         {most_played_song} ({most_played_count} plays)")
print(f"Least played:        {least_played_song} ({least_played_count} plays)")


# REFLECTION

print("\n\n" + "=" * 60)
print("WORKSHOP COMPLETE!")
print("=" * 60)

# Reflection:
# 1. The Grocery Analyzer felt most real to me because I often buy groceries 
# and keep track of what I spend. The discounts and adding items as I shop 
# remind me of how shopping works in real life.

# 2. Loops make handling data much easier because they save us from writing the same code over and over. 
# Instead of repeating, we can use loops to process many items quickly and neatly, which makes the code easier to understand and work with.

# 3. The hardest part was keeping track of the positions in the lists, especially when working with two lists like students and grades. 
# It was easy to get mixed up, and I think using dictionaries might have helped. 
# But doing it this way helped me understand how loops work with collections.

# 4. If I want to expand the Student Tracker, I would add features like converting scores to letter grades, 
# tracking attendance, calculating weighted averages, and making a report card. 
# I might also save the data to a file so I don’t lose it when I turn off the program.