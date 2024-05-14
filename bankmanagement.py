import random

class BankAccount:
    loan_feature_enabled = True

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.generate_account_number()
        self.transaction_history = []
        self.loan_taken = 0

    def generate_account_number(self):
        return random.randint(10000, 99999)

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount to deposit.")
        else:
            self.balance += amount
            self.transaction_history.append(f'Deposit: {amount}')
            print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount to withdraw.")
        elif amount > self.balance:
            print("Withdrawal amount exceeded.")
        else:
            self.balance -= amount
            self.transaction_history.append(f'Withdraw: {amount}')
            print(" Withdrawal successful.")

    def check_balance(self):
        return self.balance

    def view_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.balance += amount
            self.loan_taken += 1
            self.transaction_history.append(f'Loan Taken: {amount}')
            print("Loan taken successfully.")
        else:
            print("You have taken the maximum number of loans.")

    def transfer(self, amount, other_account):
        if amount <= 0:
            print("Invalid amount to transfer.")
        elif amount > self.balance:
            print("You do not have sufficient funds to transfer.")
        else:
            self.withdraw(amount)
            other_account.deposit(amount)
            self.transaction_history.append(f"Transferred: {amount} to account {other_account.name}")
            print("Transfer successful.")

class Admin:
    def __init__(self):
        self.accounts = []

    def create_account(self, name, email, address, account_type):
        account = BankAccount(name, email, address, account_type)
        self.accounts.append(account)
        return account.account_number

    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print("Account deleted successfully.")
                break
        else:
            print("Account not found.")

    def view_all_accounts(self):
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Name: {account.name}")

    def total_balance(self):
        total = sum(account.balance for account in self.accounts)
        print("Total Bank Balance:", total)

    def total_loan_amount(self):
        total = sum(account.balance for account in self.accounts if account.loan_taken > 0)
        print("Total Loan Amount:", total)

    def toggle_loan_feature(self):
        BankAccount.loan_feature_enabled = not BankAccount.loan_feature_enabled
        status = "enabled" if BankAccount.loan_feature_enabled else "disabled"
        print(f"Loan feature is now {status}.")

admin = Admin()

def user_operations(user):
    while True:
        print("\nUser Operations")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Check Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the amount to deposit: "))
            user.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            user.withdraw(amount)
        elif choice == "3":
            print("Available Balance:", user.check_balance())
        elif choice == "4":
            print("Transaction History:")
            user.view_transaction_history()
        elif choice == "5":
            if not user.loan_taken:
                amount = float(input("Enter the loan amount: "))
                user.take_loan(amount)
            else:
                print("You have already taken maximum number of loans.")
        elif choice == "6":
            to_account_number = input("Enter the account number to transfer: ")
            amount = float(input("Enter the amount to transfer: "))
            other_account = None 
            if other_account:
                user.transfer(amount, other_account)
            else:
                print("Account does not exist.")
        elif choice == "7":
            print("Logging out from user account.")
            break
        else:
            print("Invalid choice. Please try again.")

while True:
    print("\nWelcome to the Banking Management System")
    print("1. User Login")
    print("2. Admin Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter your account type (Savings/Current): ")
        user = BankAccount(name, email, address, account_type)
        user_operations(user)
    elif choice == "2":
        password = input("Enter admin password: ")
        if password == "admin123":  
            while True:
                print("\nAdmin Operations")
                print("1. Create Account")
                print("2. Delete Account")
                print("3. View All Accounts")
                print("4. Check Total Balance")
                print("5. Check Total Loan Amount")
                print("6. Toggle Loan Feature")
                print("7. Logout")
                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    name = input("Enter user's name: ")
                    email = input("Enter user's email: ")
                    address = input("Enter user's address: ")
                    account_type = input("Enter user's account type (Savings/Current): ")
                    account_number = admin.create_account(name, email, address, account_type)
                    print(f"Account created successfully. Account number: {account_number}")
                elif admin_choice == "2":
                    account_number = input("Enter account number to delete: ")
                    admin.delete_account(account_number)
                elif admin_choice == "3":
                    admin.view_all_accounts()
                elif admin_choice == "4":
                    admin.total_balance()
                elif admin_choice == "5":
                    admin.total_loan_amount()
                elif admin_choice == "6":
                    admin.toggle_loan_feature()
                elif admin_choice == "7":
                    print("Logging out from admin account.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Incorrect password.")
    elif choice == "3":
        print("Thank you for using the Banking Management System.")
        break
    else:
        print("Invalid choice.")
