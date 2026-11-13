
# Import transaction functions and the shared transaction list.
from transactions import (
    add_transaction,
    view_transactions,
    delete_transaction,
    edit_transaction,
    search_transactions,
    transactions
)

# Import financial statistics and data storage functions.
from finance_statistics import display_statistics
from storage import save_transactions, load_transactions

# Define available categories for income and expenses.
INCOME_CATEGORIES = ["Salary", "Business", "Investments", "Other"]
EXPENSE_CATEGORIES = ["Groceries", "Transport", "Entertainment", "Bills", "Other"]


# Display available categories and allow the user to select one.
def select_category(categories):
    print("\nAvailable categories:")

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    try:
        choice = int(input("Select a category: "))

        # Return the selected category if the choice is valid.
        if 1 <= choice <= len(categories):
            return categories[choice - 1]

        print("Invalid category selection.")

    except ValueError:
        print("Please enter a valid number.")

    return None


# Collect information and create a new income transaction.
def add_income():
    try:
        amount = float(input("Enter income amount: "))
        description = input("Enter income description: ").strip()

        # Check that the amount and description are valid.
        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if not description:
            print("Description cannot be empty.")
            return

        category = select_category(INCOME_CATEGORIES)

        # Add the transaction and save the updated data.
        if category:
            add_transaction("Income", amount, description, category)
            save_transactions(transactions)

    except ValueError:
        print("Please enter a valid number.")


# Collect information and create a new expense transaction.
def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ").strip()

        # Check that the amount and description are valid.
        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if not description:
            print("Description cannot be empty.")
            return

        category = select_category(EXPENSE_CATEGORIES)

        # Add the transaction and save the updated data.
        if category:
            add_transaction("Expense", amount, description, category)
            save_transactions(transactions)

    except ValueError:
        print("Please enter a valid number.")


# Display the main menu with all available application features.
def display_menu():
    print("\n================================")
    print("     PERSONAL EXPENSE TRACKER")
    print("================================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Statistics")
    print("5. Delete Transaction")
    print("6. Edit Transaction")
    print("7. Search Transactions")
    print("8. Exit")
    print("================================")


# Main application function that controls the program.
def main():
    # Load previously saved transactions when the application starts.
    transactions.extend(load_transactions())

    try:
        while True:
            display_menu()

            choice = input("Select an option: ")

            # Execute the selected application function.
            if choice == "1":
                add_income()
            elif choice == "2":
                add_expense()
            elif choice == "3":
                view_transactions()
            elif choice == "4":
                display_statistics(transactions)
            elif choice == "5":
                delete_transaction()
                save_transactions(transactions)
            elif choice == "6":
                edit_transaction(INCOME_CATEGORIES, EXPENSE_CATEGORIES)
                save_transactions(transactions)
            elif choice == "7":
                search_transactions()
            elif choice == "8":
                print("Thank you for using Personal Expense Tracker!")
                break
            else:
                print("Invalid option. Please try again.")

    # Handle interruptions without displaying a full error traceback.
    except KeyboardInterrupt:
        print("\nApplication interrupted. Goodbye!")


# Start the application when this file is executed directly.
if __name__ == "__main__":
    main()
