import unittest

from transactions import (
    add_transaction,
    delete_transaction,
    transactions
)


class TestTransactions(unittest.TestCase):

    def setUp(self):
        transactions.clear()

    def test_add_income_transaction(self):
        add_transaction("Income", 1500, "Monthly salary", "Salary")

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["type"], "Income")
        self.assertEqual(transactions[0]["amount"], 1500)
        self.assertEqual(transactions[0]["description"], "Monthly salary")

    def test_add_expense_transaction(self):
        add_transaction("Expense", 50, "Groceries", "Groceries")

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["type"], "Expense")
        self.assertEqual(transactions[0]["amount"], 50)

    def test_transaction_date(self):
        add_transaction("Income", 100, "Test income", "Salary")

        self.assertIn("date", transactions[0])

    def test_multiple_transactions(self):
        add_transaction("Income", 1500, "Salary", "Salary")
        add_transaction("Expense", 100, "Shopping", "Other")

        self.assertEqual(len(transactions), 2)

    def test_delete_transaction(self):
        add_transaction("Income", 1500, "Salary", "Salary")

        transactions.pop(0)

        self.assertEqual(len(transactions), 0)


if __name__ == "__main__":
    unittest.main()
