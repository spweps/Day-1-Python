class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate = .0025, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= amount
        else:
            print("You have insufficient funds: Charging $5")
            self.balance -= 5
        return self

    def make_loan(self, user, amount):
        self.balance -= amount
        user.balance += amount
        return self

    def account_total(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance += (self.balance*self.int_rate)
        return self
    
    #def prnt_all(BankAccount, ):
    
class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate=.0025, balance = 0)

    def deposit(self, amount):
        self.account.deposit(amount)
        return self

    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def make_loan(self, user, amount):
        self.account.make_loan(user, amount)
        return self

    def account_total(self):
        print(self.account.account_total())
        return self

scott = User("Scott Parry Westerbeck", "scott.westerbeck@gmail.com")
jessica = User("Jessica Beisler", "jessica.b@beislerimages.com")
silvia = User("Silvia Patricia Mariescurrena", "silmpat81@gmail.com")

scott.deposit(25000).deposit(1200).deposit(100000).withdraw(1500).withdraw(2200).withdraw(15000).make_loan(jessica, 25000)
scott.account_total()

jessica.deposit(100000).deposit(100000).deposit(100000).withdraw(25000).deposit(100000).withdraw(1200).withdraw(1500).withdraw(2000)
jessica.account_total()

silvia.deposit(1000000).deposit(1000000).deposit(1000000).withdraw(2500).withdraw(5000).withdraw(1200).withdraw(5000).deposit(1000000)
silvia.account_total()
