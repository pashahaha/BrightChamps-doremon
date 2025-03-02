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
            return self.balance
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully")
            print(f"Current balance is {self.balance}")
            return self.balance
        else:
            print("Invalid amount")

    def get_balance(self):
        return self.balance
    
    def get_account_number(self):
        return self.account_number
    
    def get_account_holder(self):
        return self.account_holder
    
    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

#example
account1 = BankAccount("12345", "John", 1000.0)
account2 = BankAccount("98765", "Irfan", 2500.0)

account1.deposit(500.0)
account2.withdraw(2000.0)
print(account1.account_number)

account1.display_account_info()
print()
account2.display_account_info()

print(account1.get_balance())
print(account1.get_account_number())