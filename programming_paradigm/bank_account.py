# bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance  # Initialize with an optional balance (defaults to 0)

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account if funds are sufficient."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")
