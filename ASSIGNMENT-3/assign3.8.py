# Demonstrate use of isinstance() with a class.
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, Dog))   
print(isinstance(dog, Animal))  
