# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize the account balance (default to 0 if not provided)
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposits the specified amount into the account"""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraws the specified amount from the account if funds are sufficient"""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Displays the current balance in a user-friendly format"""
        print(f"Current Balance: ${self.account_balance:.2f}")
