
num = int(input("Enter a number: "))


if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")


if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
