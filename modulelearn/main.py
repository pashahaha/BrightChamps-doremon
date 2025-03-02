import math #module
import newmodule

x = math.sqrt(100)
print(x)

y = dir(math)
print(y)

print ()
newmodule.greeting("Irfan")
print()
newmodule.age(15)

n1 = int(input("Enter the number 1:"))
n2 = int(input("Enter the number 2:"))

result = newmodule.sum_numbers(n1, n2)
print(result)  