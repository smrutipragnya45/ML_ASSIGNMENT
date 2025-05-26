# Demonstrate method overriding in inheritance.
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def show(self):
        print("Child class")

child = Child()
child.show()