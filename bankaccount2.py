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
            print("You have insufficient funds")
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
    
scott = BankAccount(.0025, 0)
jessica = BankAccount(.0025, 0)
silvia = BankAccount(.0025, 0)

scott.deposit(25000).deposit(1200).deposit(100000).withdraw(1500).withdraw(2200).withdraw(15000)
scott.account_total()

jessica.deposit(100000).deposit(100000).deposit(100000).withdraw(25000).deposit(100000).withdraw(1200).withdraw(1500).withdraw(2000)
jessica.account_total()

silvia.deposit(1000000).deposit(1000000).deposit(1000000).withdraw(2500).withdraw(5000).withdraw(1200).withdraw(5000).deposit(1000000)
silvia.account_total()
