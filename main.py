def display_menu():
    print("\n================================")
    print("     PERSONAL EXPENSE TRACKER")
    print("================================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Exit")
    print("================================")


def main():
    while True:
        display_menu()

        choice = input("Select an option: ")

        if choice == "1":
            print("Income feature coming soon!")
        elif choice == "2":
            print("Expense feature coming soon!")
        elif choice == "3":
            print("Transaction feature coming soon!")
        elif choice == "4":
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()