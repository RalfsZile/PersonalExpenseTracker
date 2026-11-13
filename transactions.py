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