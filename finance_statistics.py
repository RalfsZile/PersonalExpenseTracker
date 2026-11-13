def calculate_total_income(transactions):
    total = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "Income"
    )

    return total


def calculate_total_expenses(transactions):
    total = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "Expense"
    )

    return total


def calculate_balance(transactions):
    income = calculate_total_income(transactions)
    expenses = calculate_total_expenses(transactions)

    return income - expenses


def display_statistics(transactions):
    total_income = calculate_total_income(transactions)
    total_expenses = calculate_total_expenses(transactions)
    balance = calculate_balance(transactions)

    print("\n========== FINANCIAL STATISTICS ==========")
    print(f"Total income:    €{total_income:.2f}")
    print(f"Total expenses:  €{total_expenses:.2f}")
    print(f"Current balance: €{balance:.2f}")
    print("==========================================")