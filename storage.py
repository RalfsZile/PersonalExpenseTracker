import json
import os

FILE_NAME = "transactions.json"


def save_transactions(transactions):
    with open(FILE_NAME, "w") as file:
        json.dump(transactions, file, indent=4)

    print("\nTransactions saved successfully!")


def load_transactions():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Could not load transaction data.")
        return []
