class Bank:
    def __init__(self,account_no,name,balance):
        self.account_no=account_no
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance += amount
        print("Deposited:",amount)

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance += amount
            print("Withdrawn:",amount)
        else:
            print("Insufficient Balance!")

    def display(self):
        print("\nAccount Number:",self.account_no)
        print("Account Holder:",self.name)
        print("Balance:",self.balance)
sanima_bank = Bank(account_no="12345678",name="Aakash Thakur" ,balance=5000000)
print(sanima_bank.name)
print(sanima_bank.account_no)
print(sanima_bank.balance)
