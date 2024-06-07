from Account import BankAccount
class ChildrensAccount(BankAccount):
    def _init_(self, account_number, account_custodian, balance):
        super()._init_(account_number, account_custodian, balance)
        self.__interest_rate = 0.007

    def deposit(self, amount):
        super().deposit(amount)
        interest = amount * self.__interest_rate
        super().deposit(interest)
        return super().get_balance()

    def withdraw(self, amount):
        print("Withdrawal not allowed for Children's account")