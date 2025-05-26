# Use super() to call a parent class method.
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def show(self):
        super().show()
        print("Child class")

child = Child()
child.show()