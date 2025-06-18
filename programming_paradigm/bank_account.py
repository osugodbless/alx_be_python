class BankAccount:
    def __init__(self, account_balance):
        self.__account_balance = 250

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if amount == 0:
            print("Withdrawal must be greater than 0")
            return True
        elif (self.__account_balance - amount) >= 1:
            self.__account_balance -= amount
            return True

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:,.2f}")
