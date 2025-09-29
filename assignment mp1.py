
current_balance = float(input("Enter your current balance: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))

if withdrawal_amount <= 0:
    print("Error: Invalid withdrawal")
elif withdrawal_amount > current_balance:
    print("Error: Insufficient funds")
else:
    new_balance = current_balance - withdrawal_amount
    print("New balance:", new_balance)
