
from bankaccount2 import BankAccount


class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
        self.account = BankAccount 

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def make_loan(self, user, amount):
        self.account_balance -= amount
        user.account_balance += amount
        return self

    def account_total(self):
        print(self.account_balance)
        return self
        
scott = User("Scott Parry Westerbeck", "scott.westerbeck@gmail.com")
jessica = User("Jessica Beisler", "jessica.b@beislerimages.com")
silvia = User("Silvia Patricia Mariescurrena", "silmpat81@gmail.com")

scott.make_deposit(25000).make_deposit(100000).make_deposit(15000).make_loan(jessica, 25000)
jessica.make_deposit(100000).make_deposit(200000).make_deposit(1000000)
silvia.make_deposit(1000000000).make_deposit(20000).make_deposit(15000).make_loan(scott, 25000)


scott.account_total()
jessica.account_total()
silvia.account_total()

scott.make_loan(jessica, 25000)
scott.account_total()
jessica.account_total()
silvia.account_total()
