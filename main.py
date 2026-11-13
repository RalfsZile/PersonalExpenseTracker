transactions = []

INCOME_CATEGORIES = ["Salary", "Business", "Investments", "Other"]
EXPENSE_CATEGORIES = ["Groceries", "Transport", "Entertainment", "Bills", "Other"]


def add_transaction(transaction_type, amount, description, category):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "description": description,
        "category": category
    }

    transactions.append(transaction)
    print("\nTransaction added successfully!")


def select_category(categories):
    print("\nAvailable categories:")

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    try:
        choice = int(input("Select a category: "))

        if 1 <= choice <= len(categories):
            return categories[choice - 1]

        print("Invalid category selection.")

    except ValueError:
        print("Please enter a valid number.")

    return None


def add_income():
    try:
        amount = float(input("Enter income amount: "))
        description = input("Enter income description: ").strip()

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if not description:
            print("Description cannot be empty.")
            return

        category = select_category(INCOME_CATEGORIES)

        if category:
            add_transaction("Income", amount, description, category)

    except ValueError:
        print("Please enter a valid number.")


def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ").strip()

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if not description:
            print("Description cannot be empty.")
            return

        category = select_category(EXPENSE_CATEGORIES)

        if category:
            add_transaction("Expense", amount, description, category)

    except ValueError:
        print("Please enter a valid number.")


def calculate_total_income():
    total = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "Income"
    )

    return total

def calculate_total_expenses():
    total = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "Expense"
    )

    return total

def calculate_balance():
    balance = calculate_total_income() - calculate_total_expenses()
    return balance

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
        print(f"Category: {transaction['category']}")

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