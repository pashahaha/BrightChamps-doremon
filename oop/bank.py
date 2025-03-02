from encapsulation import BankAccount

print("Welcome to the bank")

john = BankAccount("12345", "John", 1000.0)
print(john.display_account_info())
print(john.deposit(500.0))
print(john.withdraw(200.0))

print()
print(john.display_account_info())