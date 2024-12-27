from auth import register_user, login_user
from transactions import add_transaction, view_transactions, delete_transaction
from reports import generate_report, calculate_savings
from budget import set_budget, check_budget
from backup_restore import backup_data, restore_data 

def handle_transactions(user_id):
    while True:
        print("\nTransactions Menu:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Delete Transaction")
        print("4. Back to Main Menu")

        choice = input("select an option: ")

        if choice == "1":
            try:
                t_type = input("Enter transaction type (income/expense): ").lower()
                category = input("Enter category: ")
                amount = float(input("Enter amount: "))
                date = input("Enter date (YYYY-MM_DD):")
                add_transaction(user_id, t_type,category,amount,date)
            except ValueError:
                print("Invalid input. Please try again.")

        elif choice == "2":
            view_transactions(user_id)

        elif choice =="3":
            try:
                transaction_id = int(input("Enter transaction ID to delete:"))
                delete_transaction(user_id,transaction_id)
            except ValueError:
                print("Invalid input. Please try again.")

        elif choice == "4":
            return

        else:
            print("Invalid option.Please try again.")    

def main():
    print("Welcome to the Finance Manager App!")

    # User authentication
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_id = login_user(username, password)
            if user_id:
                break

        elif choice == "3":
            print("Goodbye!")
            return

        else:
            print("Invalid option. Please try again.")

    # Main menu after login
    while True:
        print("\nMain Menu:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Delete Transaction")
        print("4. Generate Report")
        print("5. Calculate Savings")
        print("6. Set Budget")
        print("7. Check Budget")
        print("8. Backup Data")
        print("9. Restore Data")
        print("10. Logout")
        print("11. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            t_type = input("Enter transaction type (income/expense): ").lower()
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction(user_id, t_type, category, amount, date)

        elif choice == "2":
            view_transactions(user_id)

        elif choice == "3":
            transaction_id = int(input("Enter transaction ID to delete: "))
            delete_transaction(user_id, transaction_id)

        elif choice == "4":
            period = input("Generate report for (monthly/yearly): ").lower()
            generate_report(user_id, period)

        elif choice == "5":
            calculate_savings(user_id)

        elif choice == "6":
            category = input("Enter category for the budget: ")
            amount = float(input("Enter budget amount: "))
            set_budget(user_id, category, amount)

        elif choice == "7":
            check_budget(user_id)

        elif choice == "8":
            backup_data()

        elif choice == "9":
            restore_data()

        elif choice == "10":
            print("Logged out successfully.")
            main()  # Restart for another user login
            return

        elif choice == "11":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()