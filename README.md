# Personal Expense Tracker

A Python-based command-line application for managing personal income and expenses. The application uses an SQLite database to store financial transactions and provides tools for tracking and analyzing personal finances.

## Features

- Add income and expense transactions.
- Assign categories to transactions.
- View all recorded transactions.
- Calculate total income and expenses.
- Display the current financial balance.
- Edit and delete transactions.
- Search transactions by description.
- Store transaction data in an SQLite database.
- Apply database migrations to manage database structure.
- Run automated unit tests.
- Automatically execute tests through GitHub Actions.

## Technologies Used

- Python 3
- SQLite
- SQL
- Git and GitHub
- GitHub Actions
- unittest

## Project Structure

```text
PersonalExpenseTracker/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── migrations/
│   └── 001_create_transactions.sql
│
├── tests/
│   ├── test_statistics.py
│   ├── test_transactions.py
│   └── test_storage.py
│
├── main.py
├── transactions.py
├── finance_statistics.py
├── storage.py
├── migrate.py
├── .gitignore
└── README.md
```

## Installation and Usage

1. Clone the repository:

```bash
git clone https://github.com/RalfsZile/PersonalExpenseTracker.git
```

2. Open the project directory:

```bash
cd PersonalExpenseTracker
```

3. Apply database migrations:

```bash
python migrate.py
```

4. Start the application:

```bash
python main.py
```

## Database Migrations

The application uses SQLite for transaction storage.

Database migrations are stored in the `migrations` directory. Each SQL migration file defines a database structure change.

The `migrate.py` script checks which migrations have already been applied and executes only new migrations.

Applied migrations are recorded in the `schema_migrations` table.

## Automated Testing

The project uses Python's built-in `unittest` framework.

Run all tests with:

```bash
python -m unittest discover -s tests -v
```

The test suite covers transaction management, financial statistics, and database storage.

## Continuous Integration

GitHub Actions automatically runs the unit tests whenever changes are pushed to the `main` branch or a pull request is opened targeting `main`.

The workflow is configured in:

```text
.github/workflows/tests.yml
```

## Data Storage

Financial transactions are stored locally in the `expenses.db` SQLite database.

The database file is excluded from version control to prevent personal financial data from being uploaded to GitHub.

## Author

Ralfs Zīle