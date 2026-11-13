import sqlite3
import os

# Name of the SQLite database file.
DATABASE_NAME = "expenses.db"

# Folder containing the SQL migration files.
MIGRATIONS_FOLDER = "migrations"


def run_migrations():
    # Connect to the SQLite database.
    connection = sqlite3.connect(DATABASE_NAME)

    # Create a table to keep track of applied migrations.
    connection.execute("""
        CREATE TABLE IF NOT EXISTS schema_migrations (
            version TEXT PRIMARY KEY,
            applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Get all migration files in alphabetical order.
    migration_files = sorted(os.listdir(MIGRATIONS_FOLDER))

    for filename in migration_files:
        # Only process files containing SQL commands.
        if not filename.endswith(".sql"):
            continue

        version = filename

        # Check whether this migration has already been applied.
        result = connection.execute(
            "SELECT version FROM schema_migrations WHERE version = ?",
            (version,)
        ).fetchone()

        # Skip migrations that have already been executed.
        if result:
            continue

        migration_path = os.path.join(MIGRATIONS_FOLDER, filename)

        # Read the SQL commands from the migration file.
        with open(migration_path, "r", encoding="utf-8") as file:
            sql_script = file.read()

        try:
            # Execute the migration inside a database transaction.
            connection.executescript("BEGIN;\n" + sql_script)

            # Record the successfully applied migration.
            connection.execute(
                "INSERT INTO schema_migrations (version) VALUES (?)",
                (version,)
            )

            # Save the changes to the database.
            connection.commit()
            print(f"Applied migration: {filename}")

        except sqlite3.Error as error:
            # Undo changes if the migration fails.
            connection.rollback()
            print(f"Migration failed: {error}")
            connection.close()
            return

    # Close the database connection.
    connection.close()
    print("Database migrations completed.")


# Run migrations when this file is executed directly.
if __name__ == "__main__":
    run_migrations()
