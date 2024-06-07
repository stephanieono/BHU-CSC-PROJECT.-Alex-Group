from Account import BankAccount
class StudentAccount(BankAccount):
    def _init_(self, account_number, account_custodian, balance):
        super()._init_(account_number, account_custodian, balance)

    def deposit(self, amount):
        if amount > 50000:
            print("Deposit limit exceeded")
        super().deposit(amount)
        return super().get_balance()

    def withdraw(self, amount):
        if amount > 2000:
            print("Withdrawal limit exceeded")
        super().withdraw(amount)
        return super().get_balance()