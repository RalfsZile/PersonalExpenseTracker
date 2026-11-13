
# Import modules for working with JSON files and file paths.
import json
import os

# Define the file used to store transaction information.
FILE_NAME = "transactions.json"


# Save all transactions to the JSON file.
def save_transactions(transactions):
    # Open the file in write mode and convert transactions into JSON.
    with open(FILE_NAME, "w") as file:
        json.dump(transactions, file, indent=4)

    print("\nTransactions saved successfully!")


# Load previously saved transactions from the JSON file.
def load_transactions():
    # Check whether the transaction file exists.
    if not os.path.exists(FILE_NAME):
        return []

    try:
        # Read the JSON file and convert its contents into Python data.
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    # Handle invalid JSON data or file access errors.
    except (json.JSONDecodeError, OSError):
        print("Could not load transaction data.")
        return []
