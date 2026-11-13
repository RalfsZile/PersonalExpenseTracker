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
    else:
        for transaction in transactions:
            print(transaction)


def main():
    while True:
        display_menu()

        choice = input("Select an option: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            print("Expense feature coming soon!")
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()