import unittest
import os
import sqlite3
import storage

# Import the storage functions being tested.
from storage import save_transactions, load_transactions


class TestStorage(unittest.TestCase):

    def setUp(self):
        # Create a separate database for testing.
        self.test_database = "test_expenses.db"
        self.original_database = storage.DATABASE_NAME
        storage.DATABASE_NAME = self.test_database

        # Create the transactions table in the test database.
        connection = sqlite3.connect(self.test_database)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL
            )
        """)
        connection.commit()
        connection.close()

    def tearDown(self):
        # Restore the original database configuration.
        storage.DATABASE_NAME = self.original_database

        # Delete the temporary test database.
        if os.path.exists(self.test_database):
            os.remove(self.test_database)

    def test_save_transactions(self):
        # Prepare an example income transaction.
        transactions = [
            {
                "type": "Income",
                "amount": 1500,
                "description": "Salary",
                "category": "Salary",
                "date": "2026-11-13"
            }
        ]

        # Save the transaction and verify that it exists.
        save_transactions(transactions)

        self.assertEqual(len(load_transactions()), 1)

    def test_load_transactions(self):
        # Prepare an example expense transaction.
        transactions = [
            {
                "type": "Expense",
                "amount": 50,
                "description": "Groceries",
                "category": "Groceries",
                "date": "2026-11-13"
            }
        ]

        # Save and retrieve the transaction.
        save_transactions(transactions)
        result = load_transactions()

        # Check that the retrieved data matches the original data.
        self.assertEqual(result, transactions)

    def test_empty_database(self):
        # Check that an empty database returns an empty list.
        result = load_transactions()

        self.assertEqual(result, [])


# Run the tests when this file is executed directly.
if __name__ == "__main__":
    unittest.main()
