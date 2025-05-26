# Demonstrate constructor overloading using default arguments.
class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

p1 = Person()
p2 = Person("Alice")
p3 = Person("Bob", 25)
print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)