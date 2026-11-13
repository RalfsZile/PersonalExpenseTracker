# Personal Expense Tracker

## 1. Project Description

Personal Expense Tracker is a Python application designed to help users manage their personal finances. It allows users to record income and expenses, organize transactions into categories, and monitor their financial balance.

The application uses JSON files to store transaction information, allowing data to remain available after the program is closed.

## 2. Features

- Add income transactions.
- Add expense transactions.
- View all recorded transactions.
- Edit existing transactions.
- Delete transactions.
- Search transactions by description.
- Organize transactions into categories.
- Automatically record transaction dates.
- Calculate total income and expenses.
- Display the current financial balance.
- Save and load transaction data using JSON.
- Automated tests using Python's unittest framework.

## 3. Technologies Used

- Python 3
- JSON
- Git
- GitHub
- unittest

## 4. Project Structure

- `main.py` – Main application and navigation menu.
- `transactions.py` – Transaction management functionality.
- `finance_statistics.py` – Financial calculations and statistics.
- `storage.py` – Saving and loading transaction data.
- `transactions.json` – Automatically generated transaction storage file.
- `tests/` – Automated application tests.
  - `test_statistics.py`
  - `test_transactions.py`
  - `test_storage.py`

## 5. Installation and Usage

1. Clone the repository from GitHub.
2. Open the project directory.
3. Make sure Python 3 is installed.
4. Run the application using:

   `python main.py`

5. Select an option from the application menu.

## 6. Running Automated Tests

The project includes automated tests using Python's built-in unittest library.

To execute all tests, run:

`python -m unittest discover -s tests -v`

The tests verify financial calculations, transaction management, and JSON storage functionality.

## 7. Data Storage

Transaction information is stored locally in `transactions.json`.

The application automatically loads previously saved transactions when it starts and saves changes when transactions are added, edited, or deleted.

## 8. Author

Personal Expense Tracker was developed as an educational project for school purposes.