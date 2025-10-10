# Defining a bank account class with basic functionalities
# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a new bank account with an optional starting balance.
        """
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """
        Deposit a positive amount into the account.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw the specified amount if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def display_balance(self):
        """
        Print the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance}")
