pin = input("Enter PIN: ")

if pin == "4321":
    option = input("Choose (balance/withdraw/deposit): ")
    if option == "balance":
        print("Your balance is $500")
    elif option == "withdraw":
        amount = int(input("Enter amount: "))
        if amount <= 500:
            print("Withdrawal successful")
        else:
            print("Insufficient funds")
    elif option == "deposit":
        amount = int(input("Enter deposit amount: "))
        print("Deposit successful")
    else:
        print("Invalid option")
else:
    pin = input("Wrong PIN. Try again: ")
    if pin == "4321":
        option = input("Choose (balance/withdraw/deposit): ")
        if option == "balance":
            print("Your balance is $500")
        elif option == "withdraw":
            amount = int(input("Enter amount: "))
            if amount <= 500:
                print("Withdrawal successful")
            else:
                print("Insufficient funds")
        elif option == "deposit":
            amount = int(input("Enter deposit amount: "))
            print("Deposit successful")
        else:
            print("Invalid option")
    else:
        print("Account locked. Too many wrong attempts.")
4321