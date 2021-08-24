class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("User: "+ str(self.name) + ", Balance: "+ str(self.account_balance))

    def transfer_money(self, amount, User):
        self.account_balance -= amount
        User.account_balance += amount

Mario = User("Mario Lopez", "mario@python.com")
Ana = User("Ana Luisa", "ana@javascript.com")
Ryan = User("Ryan Garcia", "noboxingnolife@python.com")

Mario.make_deposit(200)
Mario.make_deposit(300)
Mario.make_deposit(600)
Mario.make_withdrawal(450)
Mario.display_user_balance()

Ana.make_deposit(95)
Ana.make_deposit(471.50)
Ana.make_withdrawal(350)
Ana.make_withdrawal(4.25)
Ana.display_user_balance()

Ryan.make_deposit(100000)
Ryan.make_withdrawal(900)
Ryan.make_withdrawal(15000)
Ryan.make_withdrawal(98.75)
Ryan.display_user_balance()

Mario.transfer_money(500, Ryan)
Mario.display_user_balance()
Ryan.display_user_balance()