# FCreate a base class and derive two child classes with different methods (multilevel inheritance).
class Grandparent:
    def show_grandparent(self):
        print("Grandparent class")

class Parent(Grandparent):
    def show_parent(self):
        print("Parent class")

class Child(Parent):
    def show_child(self):
        print("Child class")

child = Child()
child.show_grandparent()
child.show_parent()
child.show_child()