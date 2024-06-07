from Account import BankAccount
class SavingsAccount(BankAccount):
    def _init_(self, account_number, account_holder, balance):
        super()._init_(account_number, account_holder, balance)
        self.__interest_rate = 0.005

    def deposit(self, amount):
        super().deposit(amount)
        interest = amount * self.__interest_rate
        super().deposit(interest)
        return super().get_balance()

    def withdraw(self, amount):
        if amount > 700000:
            print("Withdrawal limit exceeded")
        super().withdraw(amount)
        return super().get_balance()