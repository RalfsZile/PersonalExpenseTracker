# Import the unittest framework for automated testing.
import unittest

# Import financial calculation functions from the application.
from finance_statistics import (
    calculate_total_income,
    calculate_total_expenses,
    calculate_balance
)


# Create a test class for financial statistics.
class TestFinancialStatistics(unittest.TestCase):

    # Prepare sample transactions before each test.
    def setUp(self):
        self.transactions = [
            {"type": "Income", "amount": 1500},
            {"type": "Income", "amount": 500},
            {"type": "Expense", "amount": 200},
            {"type": "Expense", "amount": 100}
        ]

    # Check whether total income is calculated correctly.
    def test_calculate_total_income(self):
        result = calculate_total_income(self.transactions)
        self.assertEqual(result, 2000)

    # Check whether total expenses are calculated correctly.
    def test_calculate_total_expenses(self):
        result = calculate_total_expenses(self.transactions)
        self.assertEqual(result, 300)

    # Check whether the remaining balance is correct.
    def test_calculate_balance(self):
        result = calculate_balance(self.transactions)
        self.assertEqual(result, 1700)

    # Check whether an empty transaction list returns zero.
    def test_empty_transactions(self):
        result = calculate_balance([])
        self.assertEqual(result, 0)


# Run the tests when this file is executed directly.
if __name__ == "__main__":
    unittest.main()
