#ASSIGNMENT: BANKACCOUNT USERS

class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        int_rate = 0.01
        balance = 0
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print('Balance: $' + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0: 
            self.balance += (self.balance * self.int_rate)
            return self
    @classmethod
    def list_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()
        
class User: 
    def __init__(self, name, email_address): 
        self.name = name
        self.email = email_address
        # self.account_balance = 0 (REMOVED)
        # ADDED INSTEAD: 
        self.account = {
            "checking" : BankAccount(.01, 800),
            "savings" : BankAccount(.04, 2500)
        }
    
    #THESE METHODS NO LONGER NEEDED: 
    # def make_deposit(self, amount):
    #     self.account.deposit(amount)
    #     return self
    # def make_withdrawal(self, amount):
    #     self.account.withdraw(amount)
    #     return self

    # DISPLAY USER BALANCE METHOD CREATED: 
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}") 
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self
    # TRANSFER MONEY METHOD CREATED: 
    def transfer_money(self, amount, sender, recipient):
        sender.account_balance -= amount
        recipient.account_balance += amount
        return self




# 3 USER INSTANCES CREATED:
Danny = User("Danny Murcia", "dan@python.com")
Natasha = User("Natasha Murcia", "nat@python.com")
Pachito = User("Pachito McLekkerson", "pachi@python.com")


#DEPOSIT WITH SPECIFIED ACCOUNT: 
Danny.account['checking'].deposit(100)
Danny.display_user_balance()
# Danny.display_user_balance()


Natasha.account['savings'].deposit(2000)
Natasha.display_user_balance()

BankAccount.list_all_accounts()
















