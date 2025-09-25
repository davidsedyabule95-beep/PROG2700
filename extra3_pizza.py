size = input("Choose pizza size (small/medium/large): ")

if size == "small":
    price = 8
elif size == "medium":
    price = 10
elif size == "large":
    price = 12
else:
    print("Invalid size")
    exit()

cheese = input("Do you want extra cheese? (yes/no): ")
if cheese == "yes":
    price += 2

delivery = input("Do you want delivery? (yes/no): ")
if delivery == "yes":
    price += 3

if size == "large" and cheese == "yes" and delivery == "yes":
    print("Big order discount: -$2")
    price -= 2

print("Final price: $", price)
