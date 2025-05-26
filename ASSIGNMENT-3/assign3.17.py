# Create a class Employee with a method to display the number of employees created.
class Employee:
    count = 0

    def __init__(self, name):
        self.name = name
        Employee.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total Employees: {cls.count}")

e1 = Employee("Alice")
e2 = Employee("Bob")
Employee.display_count()
