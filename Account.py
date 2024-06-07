class BankAccount:
    def __init__(self, account_number, account_custodian, balance):
        self.__account_number = '002334876'
        self.__account_custodian = 'Prince'
        self.__balance = 1,000,000

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_account_custodian(self):
        return self.__account_custodian

