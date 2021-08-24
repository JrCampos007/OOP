class User: 
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.accounts = [BankAccount(account_name="checking", int_rate=0.01, balance=0), BankAccount(account_name="savings", int_rate=0.05, balance=0)]
    
    def make_deposit(self, account_name, amount):
        for i in self.accounts:
            if i.account_name == account_name:
                i.deposit(amount)
        return self

    def make_withdrawal(self, account_name, amount):       
        for i in self.accounts:                         
            if i.account_name == account_name:
                i.withdraw(amount)
        return self

    def display_user_balance(self, account_name):
        for i in self.accounts:                         
            if i.account_name == account_name:
                print(i.account_name, i.display_account_info())
        return self

############################### SENSEI BONUS #########################################
    def create_account(self, account_name, balance):
        self.accounts.append(BankAccount(account_name=account_name, balance=balance))
        return self

    def show_balances(self):
        for i in self.accounts:
            print(i.account_name, i.int_rate, i.balance)
        print('\n', '*'*80)
        return self
#####################################################################################
class BankAccount:
    def __init__(self, account_name, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        return self.balance 

Jose = User("Jose Antonio Campos", "cibernautico2010@hotmail.com")
Jose.make_deposit("checking", 100)
Jose.make_deposit("checking", 250)
Jose.make_deposit("savings", 210)
Jose.make_withdrawal("checking", 10)
Jose.make_withdrawal("savings", 100)

# Creating an account
Jose.create_account("vacation", 0)
Jose.show_balances()
Jose.create_account("emergency", 200)
Jose.show_balances()