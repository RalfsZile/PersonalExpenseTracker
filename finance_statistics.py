
# Calculate the total amount of all income transactions.
def calculate_total_income(transactions):
    # Add together amounts from transactions classified as income.
    total = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "Income"
    )

    return total


# Calculate the total amount of all expense transactions.
def calculate_total_expenses(transactions):
    # Add together amounts from transactions classified as expenses.
    total = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "Expense"
    )

    return total


# Calculate the remaining balance after subtracting expenses from income.
def calculate_balance(transactions):
    income = calculate_total_income(transactions)
    expenses = calculate_total_expenses(transactions)

    return income - expenses


# Display a summary of the user's financial statistics.
def display_statistics(transactions):
    # Calculate all financial values before displaying them.
    total_income = calculate_total_income(transactions)
    total_expenses = calculate_total_expenses(transactions)
    balance = calculate_balance(transactions)

    print("\n========== FINANCIAL STATISTICS ==========")
    print(f"Total income:    €{total_income:.2f}")
    print(f"Total expenses:  €{total_expenses:.2f}")
    print(f"Current balance: €{balance:.2f}")
    print("==========================================")
