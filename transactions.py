
# Import date functionality for recording transaction dates.
from datetime import date

# Store all income and expense transactions in a list.
transactions = []


# Create and store a new transaction.
def add_transaction(transaction_type, amount, description, category):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "description": description,
        "category": category,
        # Automatically assign the current date to the transaction.
        "date": date.today().strftime("%Y-%m-%d")
    }

    transactions.append(transaction)
    print("\nTransaction added successfully!")


# Display all transactions currently stored in the application.
def view_transactions():
    if not transactions:
        print("\nNo transactions found.")
        return

    print("\n========== TRANSACTIONS ==========")

    # Display each transaction with its corresponding information.
    for index, transaction in enumerate(transactions, start=1):
        print(f"\nTransaction #{index}")
        print(f"Type: {transaction['type']}")
        print(f"Amount: €{transaction['amount']:.2f}")
        print(f"Description: {transaction['description']}")
        print(f"Category: {transaction['category']}")
        print(f"Date: {transaction.get('date', 'Unknown')}")

    print("\n==================================")


# Remove a selected transaction from the transaction list.
def delete_transaction():
    if not transactions:
        print("\nNo transactions available to delete.")
        return

    view_transactions()

    try:
        choice = int(input("\nEnter transaction number to delete: "))

        # Check whether the selected transaction number exists.
        if 1 <= choice <= len(transactions):
            deleted = transactions.pop(choice - 1)
            print(f"\nDeleted transaction: {deleted['description']}")
        else:
            print("Invalid transaction number.")

    except ValueError:
        print("Please enter a valid number.")


# Allow the user to modify an existing transaction.
def edit_transaction(income_categories, expense_categories):
    if not transactions:
        print("\nNo transactions available to edit.")
        return

    view_transactions()

    try:
        choice = int(input("\nEnter transaction number to edit: "))

        # Validate the selected transaction number.
        if not 1 <= choice <= len(transactions):
            print("Invalid transaction number.")
            return

        transaction = transactions[choice - 1]

        print("\nLeave a field empty to keep its current value.")

        # Update the transaction amount if a new value is entered.
        new_amount = input(
            f"New amount (€{transaction['amount']:.2f}): "
        )

        if new_amount:
            amount = float(new_amount)

            if amount <= 0:
                print("Amount must be greater than zero.")
                return

            transaction["amount"] = amount

        # Update the transaction description.
        new_description = input(
            f"New description ({transaction['description']}): "
        ).strip()

        if new_description:
            transaction["description"] = new_description

        # Select the appropriate categories based on transaction type.
        categories = (
            income_categories
            if transaction["type"] == "Income"
            else expense_categories
        )

        print("\nAvailable categories:")

        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")

        # Allow the user to change the transaction category.
        new_category = input(
            f"New category ({transaction['category']}), or Enter to keep: "
        )

        if new_category:
            category_number = int(new_category)

            if 1 <= category_number <= len(categories):
                transaction["category"] = categories[category_number - 1]
            else:
                print("Invalid category. Keeping the original category.")

        print("\nTransaction updated successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Search for transactions using words from their descriptions.
def search_transactions():
    if not transactions:
        print("\nNo transactions available to search.")
        return

    search_term = input("\nEnter description to search: ").strip().lower()

    if not search_term:
        print("Search term cannot be empty.")
        return

    # Find transactions containing the entered search term.
    results = [
        transaction for transaction in transactions
        if search_term in transaction["description"].lower()
    ]

    if not results:
        print("\nNo matching transactions found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    # Display all transactions matching the search.
    for index, transaction in enumerate(results, start=1):
        print(f"\nResult #{index}")
        print(f"Type: {transaction['type']}")
        print(f"Amount: €{transaction['amount']:.2f}")
        print(f"Description: {transaction['description']}")
        print(f"Category: {transaction['category']}")
        print(f"Date: {transaction.get('date', 'Unknown')}")

    print("\n====================================")
