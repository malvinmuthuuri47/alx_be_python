"""
This module defines a Bankaccount class that implements methods to deposit,
withdraw, and display the current balance associated with a class instance
by persisting the changes in a text file
"""

import os

class BankAccount:
    _BALANCE_FILE = "balance.txt"

    def __init__(self, account_balance: int = 0):
        """
        This constructor reads the account_balance stored in the text file
        or initializes account_balance to 0 by default
        or to a value provided by the user when the class is
        instantiated and persists the changes in a text file specified
        as a class variable
        """
        if os.path.exists(BankAccount._BALANCE_FILE):
            with open(BankAccount._BALANCE_FILE, "r") as f:
                content = f.read().strip()
                self.account_balance = int(float(content)) if content else 0
        else:
            self.account_balance = account_balance
            with open(BankAccount._BALANCE_FILE, "w") as f:
                f.write(str(self.account_balance))

    def deposit(self, amount: int) -> None:
        """
        This method increases the account_balance associated with the
        class instance by the parameter passed to it
        """
        self.account_balance += amount
        with open(BankAccount._BALANCE_FILE, "w") as f:
            f.write(str(self.account_balance))

    def withdraw(self, amount: int) -> bool:
        """
        This method subtracts from the account_balance the amount passed
        to the class method
        """
        if self.account_balance - amount >= 0:
            self.account_balance -= amount
            with open(BankAccount._BALANCE_FILE, "w") as f:
                f.write(str(self.account_balance))
            return True
        return False

    def display_balance(self) -> None:
        """
        This method displays the value in the persisted text file after all
        the operations have been performed
        """
        print(f"Current balance: ${int(self.account_balance)}")
