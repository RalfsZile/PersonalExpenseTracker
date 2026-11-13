from transactions import add_transaction, view_transactions, transactions

INCOME_CATEGORIES = ["Salary", "Business", "Investments", "Other"]
EXPENSE_CATEGORIES = ["Groceries", "Transport", "Entertainment", "Bills", "Other"]

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


def main():
    try:
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

    except KeyboardInterrupt:
        print("\nApplication interrupted. Goodbye!")


if __name__ == "__main__":
    main()