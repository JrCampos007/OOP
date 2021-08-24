class BankAccount:
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.int_rate = int_rate
        if balance == None:
            self.balance = 0
        else:
            self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.name, "Balance =", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1+self.int_rate)
        return self

checking = BankAccount("checking", 0.0125, 15000)
savings = BankAccount("savings", .045, 20000)

checking.deposit(200).deposit(100).deposit(500).withdraw(200).yield_interest().display_account_info()
savings.deposit(250).deposit(140).withdraw(100).withdraw(50).withdraw(120).withdraw(10).yield_interest().display_account_info()
