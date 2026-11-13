transactions = []


def add_transaction(transaction_type, amount, description):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "description": description
    }

    transactions.append(transaction)
    print("\nTransaction added successfully!")


def add_income():
    try:
        amount = float(input("Enter income amount: "))
        description = input("Enter income description: ")

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        add_transaction("Income", amount, description)

    except ValueError:
        print("Please enter a valid number.")


def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        add_transaction("Expense", amount, description)

    except ValueError:
        print("Please enter a valid number.")


def display_menu():
    print("\n================================")
    print("     PERSONAL EXPENSE TRACKER")
    print("================================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Exit")
    print("================================")


def view_transactions():
    if not transactions:
        print("\nNo transactions found.")
        return

    print("\n========== TRANSACTIONS ==========")

    for index, transaction in enumerate(transactions, start=1):
        print(f"\nTransaction #{index}")
        print(f"Type: {transaction['type']}")
        print(f"Amount: €{transaction['amount']:.2f}")
        print(f"Description: {transaction['description']}")

    print("\n==================================")


def main():
    while True:
        display_menu()

        choice = input("Select an option: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()