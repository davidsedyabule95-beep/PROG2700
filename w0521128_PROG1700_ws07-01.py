

# A set stores unique data only 
club_members = {"Alice", "Bob", "Charlie"}
print("Step 2 – CREATE")
print("Initial Members:", club_members)


club_members.add("Alice")  
print("After adding duplicate 'Alice':", club_members)
print()

print("Step 3 – READ")
print("Number of Members:", len(club_members))

# Loop through all members
for member in club_members:
    print("Member:", member)


print()


print("Step 4 – UPDATE")

# Add new members
club_members.add("Diana")
print("After adding Diana:", club_members)


club_members.remove("Alice")


club_members.discard("Bob")
print("After removing Alice and Bob:", club_members)


new_members = {"Eve", "Frank", "Grace"}
club_members.update(new_members)
print("After update with multiple names:", club_members)
print()


print("Step 5 – DELETE")

# Clear all members 
club_members.clear()
print("Cleared Set:", club_members)


print()

print("Step 6 – Duplicate Email Cleanup Example")

emails = ["test@gmail.com", "admin@gmail.com", "test@gmail.com", "info@gmail.com"]
print("Original Email List:", emails)


unique_emails = set(emails)
print("Unique Emails:", unique_emails)


cleaned_list = list(unique_emails)
print("Cleaned Email List:", cleaned_list)
print()


# Reflection Questions 

# 1. How are sets different from lists or tuples?
#     Sets are unordered and do not allow duplicates.
#      Lists keep order and can contain duplicates, while tuples are ordered but immutable.

# 2. Why is it useful that sets automatically remove duplicates?
#     It helps keep data clean, especially when working with records like usernames,
#      email addresses, or unique IDs where repetition could cause problems.

# 3. What type of data might you store in a set in a real program?
#     Things like registered usernames, unique product IDs, visited URLs,
#     or even cleaned-up email lists like in the example above.
