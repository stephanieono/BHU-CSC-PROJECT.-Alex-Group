from Account import BankAccount
class CurrentAccount(BankAccount):
    def _init_(self, account_number, account_custodian, balance):
        super()._init_(account_number, account_custodian, balance)

    def deposit(self, amount):
        super().deposit(amount)
        return super().get_balance()

    def withdraw(self, amount):
        super().withdraw(amount)
        return super().get_balance()