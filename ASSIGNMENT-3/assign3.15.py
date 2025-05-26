# Demonstrate encapsulation using getter and setter.
class Person:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        if age > 0:
            self.__age = age

    def get_age(self):
        return self.__age

person = Person()
person.set_age(30)
print(person.get_age())