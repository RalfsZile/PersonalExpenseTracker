import unittest

from finance_statistics import (
    calculate_total_income,
    calculate_total_expenses,
    calculate_balance
)


class TestFinancialStatistics(unittest.TestCase):

    def setUp(self):
        self.transactions = [
            {"type": "Income", "amount": 1500},
            {"type": "Income", "amount": 500},
            {"type": "Expense", "amount": 200},
            {"type": "Expense", "amount": 100}
        ]

    def test_calculate_total_income(self):
        result = calculate_total_income(self.transactions)
        self.assertEqual(result, 2000)

    def test_calculate_total_expenses(self):
        result = calculate_total_expenses(self.transactions)
        self.assertEqual(result, 300)

    def test_calculate_balance(self):
        result = calculate_balance(self.transactions)
        self.assertEqual(result, 1700)

    def test_empty_transactions(self):
        result = calculate_balance([])
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
