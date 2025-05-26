# Create a simple class Person with name and age as attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)
print(f"Name: {person1.name}, Age: {person1.age}")