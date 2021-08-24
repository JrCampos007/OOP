class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User: "+ str(self.name) + ", Balance: "+ str(self.account_balance))
        return self

    def transfer_money(self, amount, User):
        self.account_balance -= amount
        User.account_balance += amount
        return self

Mario = User("Mario Lopez", "mario@python.com")
Ana = User("Ana Luisa", "ana@javascript.com")
Ryan = User("Ryan Garcia", "noboxingnolife@python.com")

Mario.make_deposit(200).make_deposit(300).make_deposit(600).make_withdrawal(450).display_user_balance()

Ana.make_deposit(95).make_deposit(471.50).make_withdrawal(350).make_withdrawal(4.25).display_user_balance()

Ryan.make_deposit(100000).make_withdrawal(900).make_withdrawal(15000).make_withdrawal(98.75).display_user_balance()

Mario.transfer_money(500, Ryan).display_user_balance()
Ryan.display_user_balance()