class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount {amount} deposited succesfully")
            print(f"Current balance is {self.balance}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully")
            print(f"Current balance is {self.balance}")
        else:
            print("Invalid amount")

#example
account1 = BankAccount("123456789", "John Doe", 1000.0)
account2 = BankAccount("987654321", "Irfan", 2500.0)

account1.deposit(500.0)
account2.withdraw(2000.0)
print(account1.account_number)