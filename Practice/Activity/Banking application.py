# Ubang Bank

def check():
    print(f"Your current Balance: ₹{balance}")


def withdraw(amount):
    global balance

    if amount <= 0:
        print("Cannot withdraw! Amount must be greater than 0.")

    elif amount > balance:
        print("Insufficient balance!")

    else:
        balance -= amount
        print(f"₹{amount} withdrawn successfully! 😊")


def deposit(amount):
    global balance

    if amount <= 0:
        print("Cannot deposit! Amount must be greater than 0.")

    else:
        balance += amount
        print(f"₹{amount} deposited successfully! 😊")


def history():
    print("\n====== Transaction History ======")

    if len(transactions) == 0:
        print("No transactions yet.")

    else:
        for transaction in transactions:
            print(transaction)


balance = 0
transactions = []

while True:

    print("\n====== Welcome to Ubang Bank ======\n")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Transaction History")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check()

    elif choice == "2":
        amt = int(input("Enter the amount: "))

        if amt > 0 and amt <= balance:
            withdraw(amt)
            transactions.append(f"Withdrawn: ₹{amt}")
        else:
            withdraw(amt)

    elif choice == "3":
        amt = int(input("Enter the amount: "))

        if amt > 0:
            deposit(amt)
            transactions.append(f"Deposited: ₹{amt}")
        else:
            deposit(amt)

    elif choice == "4":
        history()

    elif choice == "5":
        print("Thank you for using our service! 😊")
        break

    else:
        print("Invalid choice! 😒")