# Write a program to demonstrate polymorphism with a common method.
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

def make_sound(animal):
    animal.sound()

cat = Cat()
dog = Dog()
make_sound(cat)
make_sound(dog)