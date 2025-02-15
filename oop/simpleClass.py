"""class Car:
    def __init__(self, name, behavior):
        self.name = name
        self.behavior = behavior

car1 = Car("Ferrari", "fast")
print(car1.name)
print(car1.behavior)

car2 = Car("Porsche", "slow")
print(car2.name)
print(car2.behavior)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person1 = Person('Irfan', '20')
print(person1.name)
print(person1.age)

person2 = Person('Ali', '22')
print(person2.name)
print(person2.age)

class Fruit():
    type = "apple"
    
    def fruitmethod(self):
        print("this is a fruit")


fruit1 = Fruit()
print(fruit1.type)

fruit1.fruitmethod()



class Student:
    age = 19
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

student1 = Student("Irfan")
student1.say_hello()

student2 = Student("Ahmad")
student2.say_hello()

print(student1.age)
print(student2.age)

age = 90
print(age)
"""

class Polygon:
    def __init__ (self,sides):
        self.sides = sides
    
    def perimeter(self):
        perimeter = sum(self.sides)
        return perimeter


class Quadrilateral(Polygon):
    def info(self):
        print("This is a Quadrilateral")

class Pentagon(Polygon):
    def info(self):
        print("This is a Pentagon") 

quadobj = Quadrilateral([1,2,3,4])
print(quadobj.perimeter())

pentobj = Pentagon([1,2,3,4,5])
print(pentobj.perimeter())