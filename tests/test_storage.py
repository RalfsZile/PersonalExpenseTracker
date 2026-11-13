import unittest
import os
import json

from storage import save_transactions, load_transactions


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_transactions.json"
        import storage
        self.original_file = storage.FILE_NAME
        storage.FILE_NAME = self.test_file

    def tearDown(self):
        import storage
        storage.FILE_NAME = self.original_file

        if os.path.exists(self.test_file):
            os.remove(self.test_file)

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

    def test_load_transactions(self):
        transactions = [
            {
                "type": "Expense",
                "amount": 50,
                "description": "Groceries",
                "category": "Groceries"
            }
        ]

        with open(self.test_file, "w") as file:
            json.dump(transactions, file)

        result = load_transactions()

        self.assertEqual(result, transactions)

    def test_missing_file(self):
        result = load_transactions()

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
