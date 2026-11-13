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