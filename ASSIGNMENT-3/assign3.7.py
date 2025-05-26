# Create a class and use a method to set its attributes.
class Person:
    def set_attributes(self, name, age):
        self.name = name
        self.age = age

person = Person()
person.set_attributes("Bob", 25)
print(f"Name: {person.name}, Age: {person.age}")