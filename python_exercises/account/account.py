# def add(x, y):
#     return x + y
#
# def subtract(x, y):
#     return x - y

class Account:
    def __init__(self, name: str):
        self.balance = 0
        self.name = name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Amount cannot be deposited")

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Negative Amount cannot be withdrawn")
        elif amount > self.balance:
            raise ValueError("Are you a thief, you can not withdraw more than your balance")
        else:
            self.balance -= amount

    def load_airtime(self, airtime_amount):
        if airtime_amount < 50:
            raise ValueError("You are broke, we dont sell #40 airtime")
        self.balance -= airtime_amount

    def transfer(self, amount, account2):
        self.balance -= amount
        account2.balance += amount
