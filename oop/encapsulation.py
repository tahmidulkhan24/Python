class Bank:

    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit success")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw successful")
        else:
            print("Insufficient balance")


acc = Bank(1000)

acc.deposit(500)

acc.withdraw(200)

print("Current balance:", acc.balance)