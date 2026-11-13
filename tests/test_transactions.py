# Import the unittest framework for automated testing.
import unittest

# Import transaction functions and the shared transaction list.
from transactions import add_transaction, transactions


# Create a test class for transaction management.
class TestTransactions(unittest.TestCase):

    # Clear existing transactions before every test.
    def setUp(self):
        transactions.clear()

    # Check whether an income transaction is created correctly.
    def test_add_income_transaction(self):
        add_transaction("Income", 1500, "Monthly salary", "Salary")

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["type"], "Income")
        self.assertEqual(transactions[0]["amount"], 1500)
        self.assertEqual(transactions[0]["description"], "Monthly salary")

    # Check whether an expense transaction is created correctly.
    def test_add_expense_transaction(self):
        add_transaction("Expense", 50, "Groceries", "Groceries")

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["type"], "Expense")
        self.assertEqual(transactions[0]["amount"], 50)

    # Check whether a new transaction receives a date.
    def test_transaction_date(self):
        add_transaction("Income", 100, "Test income", "Salary")

        self.assertIn("date", transactions[0])

    # Check whether multiple transactions can be stored.
    def test_multiple_transactions(self):
        add_transaction("Income", 1500, "Salary", "Salary")
        add_transaction("Expense", 100, "Shopping", "Other")

        self.assertEqual(len(transactions), 2)

    # Check whether a transaction can be removed from the list.
    def test_delete_transaction(self):
        add_transaction("Income", 1500, "Salary", "Salary")

        transactions.pop(0)

        self.assertEqual(len(transactions), 0)


# Run the tests when this file is executed directly.
if __name__ == "__main__":
    unittest.main()
