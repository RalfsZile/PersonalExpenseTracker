import sqlite3

# Name of the SQLite database file.
DATABASE_NAME = "expenses.db"


def save_transactions(transactions):
    # Connect to the database.
    connection = sqlite3.connect(DATABASE_NAME)

    # Remove existing transactions before saving the updated list.
    connection.execute("DELETE FROM transactions")

    # Insert each transaction into the database.
    for transaction in transactions:
        connection.execute(
            """
            INSERT INTO transactions
            (type, amount, description, category, date)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                transaction["type"],
                transaction["amount"],
                transaction["description"],
                transaction["category"],
                transaction.get("date", "Unknown")
            )
        )

    # Save the changes and close the connection.
    connection.commit()
    connection.close()

    print("\nTransactions saved successfully!")


def load_transactions():
    # Connect to the database.
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Retrieve all transactions in their original order.
    cursor.execute("""
        SELECT type, amount, description, category, date
        FROM transactions
        ORDER BY id
    """)

    rows = cursor.fetchall()

    # Close the database connection.
    connection.close()

    # Convert database rows into Python dictionaries.
    return [
        {
            "type": row[0],
            "amount": row[1],
            "description": row[2],
            "category": row[3],
            "date": row[4]
        }
        for row in rows
    ]
