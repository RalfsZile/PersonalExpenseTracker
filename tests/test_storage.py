# Import libraries for testing, file management, and JSON operations.
import unittest
import os
import json

# Import functions responsible for saving and loading transactions.
from storage import save_transactions, load_transactions


# Create a test class for JSON storage functionality.
class TestStorage(unittest.TestCase):

    # Prepare a separate test file before each test.
    def setUp(self):
        self.test_file = "test_transactions.json"

        import storage

        # Temporarily change the storage filename for testing.
        self.original_file = storage.FILE_NAME
        storage.FILE_NAME = self.test_file

    # Restore the original filename after each test.
    def tearDown(self):
        import storage

        storage.FILE_NAME = self.original_file

        # Remove the temporary test file if it exists.
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    # Check whether transactions are saved to a JSON file.
    def test_save_transactions(self):
        transactions = [
            {
                "type": "Income",
                "amount": 1500,
                "description": "Salary",
                "category": "Salary"
            }
        ]

        save_transactions(transactions)

        self.assertTrue(os.path.exists(self.test_file))

    # Check whether saved transactions can be loaded correctly.
    def test_load_transactions(self):
        transactions = [
            {
                "type": "Expense",
                "amount": 50,
                "description": "Groceries",
                "category": "Groceries"
            }
        ]

        # Write sample transaction data into the temporary JSON file.
        with open(self.test_file, "w") as file:
            json.dump(transactions, file)

        result = load_transactions()

        self.assertEqual(result, transactions)

    # Check whether a missing JSON file returns an empty list.
    def test_missing_file(self):
        result = load_transactions()

        self.assertEqual(result, [])


# Run the tests when this file is executed directly.
if __name__ == "__main__":
    unittest.main()
