# Demonstrate single inheritance in Python.
class Parent:
    def show(self):
        print("This is the parent class.")

class Child(Parent):
    pass

child = Child()
child.show()