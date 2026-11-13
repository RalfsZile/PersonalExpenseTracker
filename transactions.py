transactions = []


def add_transaction(transaction_type, amount, description, category):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "description": description,
        "category": category
    }

    transactions.append(transaction)
    print("\nTransaction added successfully!")


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

def delete_transaction():
    if not transactions:
        print("\nNo transactions available to delete.")
        return

    view_transactions()

    try:
        choice = int(input("\nEnter transaction number to delete: "))

        if 1 <= choice <= len(transactions):
            deleted = transactions.pop(choice - 1)
            print(f"\nDeleted transaction: {deleted['description']}")
        else:
            print("Invalid transaction number.")

    except ValueError:
        print("Please enter a valid number.")

def edit_transaction(income_categories, expense_categories):
    if not transactions:
        print("\nNo transactions available to edit.")
        return

    view_transactions()

    try:
        choice = int(input("\nEnter transaction number to edit: "))

        if not 1 <= choice <= len(transactions):
            print("Invalid transaction number.")
            return

        transaction = transactions[choice - 1]

        print("\nLeave a field empty to keep its current value.")

        new_amount = input(
            f"New amount (€{transaction['amount']:.2f}): "
        )

        if new_amount:
            amount = float(new_amount)

            if amount <= 0:
                print("Amount must be greater than zero.")
                return

            transaction["amount"] = amount

        new_description = input(
            f"New description ({transaction['description']}): "
        ).strip()

        if new_description:
            transaction["description"] = new_description

        categories = (
            income_categories
            if transaction["type"] == "Income"
            else expense_categories
        )

        print("\nAvailable categories:")

        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")

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
